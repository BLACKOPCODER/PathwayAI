import sqlite3
import json
from datetime import datetime
import os

class DatabaseManager:
    def __init__(self, db_path="database/career_bot.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_database()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Topics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                difficulty TEXT,
                created_by INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (created_by) REFERENCES users(id)
            )
        ''')
        
        # Roadmaps table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roadmaps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                field TEXT NOT NULL,
                skill_level TEXT NOT NULL,
                interests TEXT,
                roadmap_data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        # Roadmap steps table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roadmap_steps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roadmap_id INTEGER NOT NULL,
                step_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                resources TEXT,
                video_links TEXT,
                estimated_duration TEXT,
                completed BOOLEAN DEFAULT 0,
                FOREIGN KEY (roadmap_id) REFERENCES roadmaps(id)
            )
        ''')
        
        # Tests table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                difficulty TEXT,
                created_by INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (topic_id) REFERENCES topics(id),
                FOREIGN KEY (created_by) REFERENCES users(id)
            )
        ''')
        
        # Questions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_id INTEGER NOT NULL,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                explanation TEXT,
                FOREIGN KEY (test_id) REFERENCES tests(id)
            )
        ''')
        
        # Test results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                test_id INTEGER NOT NULL,
                score REAL NOT NULL,
                total_questions INTEGER NOT NULL,
                correct_answers INTEGER NOT NULL,
                answers_data TEXT,
                taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (test_id) REFERENCES tests(id)
            )
        ''')
        
        # Insert default admin if not exists
        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        if not cursor.fetchone():
            cursor.execute('''
                INSERT INTO users (username, password, role, email)
                VALUES (?, ?, ?, ?)
            ''', ('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5aeJKc0g3zKZe', 'admin', 'admin@careerbot.com'))
            # Password is 'admin123' hashed with bcrypt
        
        cursor.execute("SELECT COUNT(*) FROM topics")
        topics_count = cursor.fetchone()[0]
        if topics_count == 0:
            cursor.execute("SELECT id FROM users WHERE username = 'admin'")
            admin_row = cursor.fetchone()
            admin_id = admin_row[0] if admin_row else None
            cursor.execute('''
                INSERT INTO topics (name, category, description, difficulty, created_by)
                VALUES (?, ?, ?, ?, ?)
            ''', ('Python Programming', 'Data Science', 'Core Python basics and fundamentals', 'Beginner', admin_id))
            topic_id = cursor.lastrowid
            cursor.execute('''
                INSERT INTO tests (topic_id, title, description, difficulty, created_by)
                VALUES (?, ?, ?, ?, ?)
            ''', (topic_id, 'Python Basics Quiz', 'A short quiz covering basic Python concepts', 'Beginner', admin_id))
            test_id = cursor.lastrowid
            cursor.execute('''
                INSERT INTO questions (test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (test_id, 'Which of the following creates a list in Python?', "my_list = [1, 2, 3]", "my_list = (1, 2, 3)", "my_list = {1, 2, 3}", "my_list = '1,2,3'", 'A', 'Lists use square brackets []'))
            cursor.execute('''
                INSERT INTO questions (test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (test_id, 'What is the output of print(2 ** 3)?', "6", "8", "9", "23", 'B', '** is exponentiation'))
            cursor.execute('''
                INSERT INTO questions (test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (test_id, 'Which keyword defines a function?', "func", "def", "function", "define", 'B', 'Functions are defined with def'))
        
        conn.commit()
        conn.close()
    
    # User Management
    def create_user(self, username, password_hash, role='user', email=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, password, role, email)
                VALUES (?, ?, ?, ?)
            ''', (username, password_hash, role, email))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def get_user(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def get_all_users(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, role, email, created_at FROM users')
        users = cursor.fetchall()
        conn.close()
        return users
    
    def delete_user(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
    
    # Topic Management
    def create_topic(self, name, category, description, difficulty, created_by):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO topics (name, category, description, difficulty, created_by)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, category, description, difficulty, created_by))
        conn.commit()
        topic_id = cursor.lastrowid
        conn.close()
        return topic_id
    
    def get_all_topics(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM topics ORDER BY category, name')
        topics = cursor.fetchall()
        conn.close()
        return topics
    
    def get_topics_by_category(self, category):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM topics WHERE category = ?', (category,))
        topics = cursor.fetchall()
        conn.close()
        return topics
    
    def delete_topic(self, topic_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM topics WHERE id = ?', (topic_id,))
        conn.commit()
        conn.close()
    
    # Roadmap Management
    def create_roadmap(self, user_id, title, field, skill_level, interests, roadmap_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO roadmaps (user_id, title, field, skill_level, interests, roadmap_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, title, field, skill_level, interests, json.dumps(roadmap_data)))
        roadmap_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return roadmap_id
    
    def add_roadmap_steps(self, roadmap_id, steps):
        conn = self.get_connection()
        cursor = conn.cursor()
        for i, step in enumerate(steps, 1):
            cursor.execute('''
                INSERT INTO roadmap_steps 
                (roadmap_id, step_number, title, description, resources, video_links, estimated_duration)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (roadmap_id, i, step['title'], step['description'], 
                  json.dumps(step.get('resources', [])), 
                  json.dumps(step.get('video_links', [])),
                  step.get('estimated_duration', 'N/A')))
        conn.commit()
        conn.close()
    
    def get_user_roadmaps(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM roadmaps WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
        roadmaps = cursor.fetchall()
        conn.close()
        return roadmaps
    
    def get_roadmap_steps(self, roadmap_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM roadmap_steps WHERE roadmap_id = ? ORDER BY step_number', (roadmap_id,))
        steps = cursor.fetchall()
        conn.close()
        return steps
    
    def update_step_completion(self, step_id, completed):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE roadmap_steps SET completed = ? WHERE id = ?', (completed, step_id))
        conn.commit()
        conn.close()
    
    # Test Management
    def create_test(self, topic_id, title, description, difficulty, created_by):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tests (topic_id, title, description, difficulty, created_by)
            VALUES (?, ?, ?, ?, ?)
        ''', (topic_id, title, description, difficulty, created_by))
        test_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return test_id
    
    def add_question(self, test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO questions 
            (test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation))
        conn.commit()
        conn.close()
    
    def get_all_tests(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT t.*, tp.name as topic_name 
            FROM tests t 
            JOIN topics tp ON t.topic_id = tp.id
            ORDER BY t.created_at DESC
        ''')
        tests = cursor.fetchall()
        conn.close()
        return tests
    
    def get_test_questions(self, test_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM questions WHERE test_id = ?', (test_id,))
        questions = cursor.fetchall()
        conn.close()
        return questions
    
    def save_test_result(self, user_id, test_id, score, total_questions, correct_answers, answers_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO test_results 
            (user_id, test_id, score, total_questions, correct_answers, answers_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, test_id, score, total_questions, correct_answers, json.dumps(answers_data)))
        conn.commit()
        conn.close()
    
    def get_user_test_history(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT tr.*, t.title as test_title, tp.name as topic_name
            FROM test_results tr
            JOIN tests t ON tr.test_id = t.id
            JOIN topics tp ON t.topic_id = tp.id
            WHERE tr.user_id = ?
            ORDER BY tr.taken_at DESC
        ''', (user_id,))
        results = cursor.fetchall()
        conn.close()
        return results
