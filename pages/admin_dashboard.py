import streamlit as st
import json
from database.db_manager import DatabaseManager
from utils.auth import AuthManager

def show_topic_management(db, auth):
    auth.require_admin()
    
    st.title("📚 Topic Management")
    
    tab1, tab2 = st.tabs(["View Topics", "Add New Topic"])
    
    with tab1:
        st.subheader("Existing Topics")
        
        topics = db.get_all_topics()
        
        if not topics:
            st.info("No topics yet. Create your first topic!")
        else:
            # Group by category
            categories = {}
            for topic in topics:
                category = topic[2]
                if category not in categories:
                    categories[category] = []
                categories[category].append(topic)
            
            for category, category_topics in categories.items():
                st.markdown(f"### 📂 {category}")
                
                for topic in category_topics:
                    topic_id = topic[0]
                    name = topic[1]
                    description = topic[3]
                    difficulty = topic[4]
                    
                    with st.expander(f"{name} ({difficulty})"):
                        st.write(f"**Description:** {description}")
                        st.write(f"**Category:** {category}")
                        st.write(f"**Difficulty:** {difficulty}")
                        
                        col1, col2 = st.columns(2)
                        
                        with col2:
                            if st.button("🗑️ Delete", key=f"delete_topic_{topic_id}"):
                                db.delete_topic(topic_id)
                                st.success("Topic deleted!")
                                st.rerun()
    
    with tab2:
        st.subheader("Create New Topic")
        
        with st.form("new_topic_form"):
            name = st.text_input("Topic Name", placeholder="e.g., Python Programming")
            
            category = st.selectbox(
                "Category",
                ["Web Development", "Data Science", "Mobile Development", 
                 "Machine Learning", "DevOps", "Cybersecurity", "Other"]
            )
            
            if category == "Other":
                category = st.text_input("Specify Category")
            
            description = st.text_area(
                "Description",
                placeholder="Brief description of the topic"
            )
            
            difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
            
            submit = st.form_submit_button("Create Topic")
            
            if submit:
                if name and category and description:
                    topic_id = db.create_topic(
                        name=name,
                        category=category,
                        description=description,
                        difficulty=difficulty,
                        created_by=st.session_state.user['id']
                    )
                    st.success(f"✅ Topic '{name}' created successfully!")
                    st.rerun()
                else:
                    st.warning("Please fill in all fields")

def show_user_management(db, auth):
    auth.require_admin()
    
    st.title("👥 User Management")
    
    users = db.get_all_users()
    
    st.write(f"Total Users: {len(users)}")
    
    # Statistics
    admin_count = sum(1 for u in users if u[2] == 'admin')
    user_count = sum(1 for u in users if u[2] == 'user')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Admins", admin_count)
    
    with col2:
        st.metric("Regular Users", user_count)
    
    st.markdown("---")
    
    # User list
    st.subheader("All Users")
    
    for user in users:
        user_id = user[0]
        username = user[1]
        role = user[2]
        email = user[3]
        created_at = user[4]
        
        with st.expander(f"{'👤' if role == 'user' else '🔧'} {username} ({role})"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Username:** {username}")
                st.write(f"**Role:** {role.capitalize()}")
            
            with col2:
                st.write(f"**Email:** {email}")
                st.write(f"**Joined:** {created_at[:10]}")
            
            # Get user statistics
            roadmaps = db.get_user_roadmaps(user_id)
            test_history = db.get_user_test_history(user_id)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Roadmaps", len(roadmaps))
            
            with col2:
                st.metric("Tests Taken", len(test_history))
            
            with col3:
                if test_history:
                    avg_score = sum([r[3] for r in test_history]) / len(test_history)
                    st.metric("Avg Score", f"{avg_score:.1f}%")
                else:
                    st.metric("Avg Score", "N/A")
            
            # Delete user (cannot delete yourself)
            if user_id != st.session_state.user['id']:
                if st.button("🗑️ Delete User", key=f"delete_user_{user_id}"):
                    if st.session_state.get(f'confirm_delete_user_{user_id}'):
                        db.delete_user(user_id)
                        st.success(f"User '{username}' deleted!")
                        st.rerun()
                    else:
                        st.session_state[f'confirm_delete_user_{user_id}'] = True
                        st.warning("Click again to confirm deletion")

def show_test_management(db, auth):
    auth.require_admin()
    
    st.title("📝 Test Management")
    
    tab1, tab2 = st.tabs(["View Tests", "Create New Test"])
    
    with tab1:
        st.subheader("Existing Tests")
        
        tests = db.get_all_tests()
        
        if not tests:
            st.info("No tests yet. Create your first test!")
        else:
            for test in tests:
                test_id = test[0]
                title = test[2]
                description = test[3]
                difficulty = test[4]
                topic_name = test[7]
                
                # Get questions count
                questions = db.get_test_questions(test_id)
                num_questions = len(questions)
                
                with st.expander(f"📄 {title} - {topic_name}"):
                    st.write(f"**Description:** {description}")
                    st.write(f"**Topic:** {topic_name}")
                    st.write(f"**Difficulty:** {difficulty}")
                    st.write(f"**Questions:** {num_questions}")
                    
                    # Show questions
                    if questions:
                        st.markdown("**Questions:**")
                        for i, q in enumerate(questions, 1):
                            with st.container():
                                st.write(f"{i}. {q[2]}")
                                st.write(f"   A) {q[3]}")
                                st.write(f"   B) {q[4]}")
                                st.write(f"   C) {q[5]}")
                                st.write(f"   D) {q[6]}")
                                st.write(f"   **Correct:** {q[7]}")
                                if q[8]:
                                    st.info(f"Explanation: {q[8]}")
                                st.markdown("---")
    
    with tab2:
        st.subheader("Create New Test")
        
        # Get all topics
        topics = db.get_all_topics()
        
        if not topics:
            st.warning("Please create topics first before creating tests!")
            return
        
        topic_names = [f"{t[1]} ({t[2]})" for t in topics]
        topic_ids = [t[0] for t in topics]
        
        selected_topic_idx = st.selectbox("Select Topic", range(len(topic_names)), format_func=lambda i: topic_names[i])
        selected_topic_id = topic_ids[selected_topic_idx]
        
        title = st.text_input("Test Title", placeholder="e.g., Python Basics Quiz")
        description = st.text_area("Test Description", placeholder="Brief description of the test")
        difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])
        
        num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=5)
        
        if st.button("Create Test Structure"):
            st.session_state.creating_test = True
            st.session_state.test_info = {
                'topic_id': selected_topic_id,
                'title': title,
                'description': description,
                'difficulty': difficulty,
                'num_questions': num_questions
            }
            st.session_state.test_questions = []
        
        # Question entry form
        if st.session_state.get('creating_test'):
            test_info = st.session_state.test_info
            
            st.markdown("---")
            st.subheader("Add Questions")
            
            for i in range(test_info['num_questions']):
                st.markdown(f"### Question {i+1}")
                
                with st.form(f"question_form_{i}"):
                    question_text = st.text_area(f"Question {i+1}", key=f"q_text_{i}")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        option_a = st.text_input("Option A", key=f"opt_a_{i}")
                        option_b = st.text_input("Option B", key=f"opt_b_{i}")
                    
                    with col2:
                        option_c = st.text_input("Option C", key=f"opt_c_{i}")
                        option_d = st.text_input("Option D", key=f"opt_d_{i}")
                    
                    correct_answer = st.selectbox("Correct Answer", ["A", "B", "C", "D"], key=f"correct_{i}")
                    explanation = st.text_area("Explanation (Optional)", key=f"exp_{i}")
                    
                    if st.form_submit_button(f"Save Question {i+1}"):
                        if question_text and option_a and option_b and option_c and option_d:
                            question_data = {
                                'question_text': question_text,
                                'option_a': option_a,
                                'option_b': option_b,
                                'option_c': option_c,
                                'option_d': option_d,
                                'correct_answer': correct_answer,
                                'explanation': explanation
                            }
                            
                            # Check if question already saved
                            if len(st.session_state.test_questions) <= i:
                                st.session_state.test_questions.append(question_data)
                            else:
                                st.session_state.test_questions[i] = question_data
                            
                            st.success(f"Question {i+1} saved!")
                        else:
                            st.error("Please fill in all required fields")
            
            # Finalize test
            st.markdown("---")
            
            if len(st.session_state.test_questions) == test_info['num_questions']:
                if st.button("✅ Finalize and Create Test", type="primary"):
                    # Create test in database
                    test_id = db.create_test(
                        topic_id=test_info['topic_id'],
                        title=test_info['title'],
                        description=test_info['description'],
                        difficulty=test_info['difficulty'],
                        created_by=st.session_state.user['id']
                    )
                    
                    # Add questions
                    for q in st.session_state.test_questions:
                        db.add_question(
                            test_id=test_id,
                            question_text=q['question_text'],
                            option_a=q['option_a'],
                            option_b=q['option_b'],
                            option_c=q['option_c'],
                            option_d=q['option_d'],
                            correct_answer=q['correct_answer'],
                            explanation=q['explanation']
                        )
                    
                    st.success(f"✅ Test '{test_info['title']}' created with {len(st.session_state.test_questions)} questions!")
                    
                    # Clear state
                    st.session_state.creating_test = False
                    st.session_state.test_info = None
                    st.session_state.test_questions = []
                    
                    st.rerun()
            else:
                st.info(f"Please save all {test_info['num_questions']} questions before finalizing.")

def main():
    db = DatabaseManager()
    auth = AuthManager(db)
    if not st.session_state.get('user'):
        with st.form("admin_login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            if submit:
                user = auth.login(username, password)
                if user and user['role'] == 'admin':
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Invalid credentials or not an admin")
        return
    with st.sidebar:
        page = st.radio("Navigate to:", ["Topic Management", "User Management", "View Tests"], key="admin_only_nav")
        if st.button("Logout"):
            auth.logout()
            st.rerun()
    if page == "Topic Management":
        show_topic_management(db, auth)
    elif page == "User Management":
        show_user_management(db, auth)
    elif page == "View Tests":
        show_test_management(db, auth)

if __name__ == "__main__":
    main()
