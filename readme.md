# PathwayAI 🎓

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**An AI-Powered Career Development & Learning Management Platform**

Create personalized learning roadmaps • Take skill assessments • Track your progress

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation)

</div>

---

## 📖 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Demo Credentials](#demo-credentials)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Customization](#customization)
- [API Reference](#api-reference)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

**PathwayAI** is a comprehensive, AI-powered learning management system designed to revolutionize career development and skill acquisition. The platform intelligently generates personalized learning roadmaps, provides structured assessments, and tracks progress across multiple career domains.

### Why PathwayAI?

- 🎯 **Personalized Learning Paths** - AI-driven roadmap generation tailored to your skill level and career goals
- 📊 **Data-Driven Insights** - Track your progress with detailed analytics and performance metrics
- 🎥 **Curated Resources** - 90+ hand-picked YouTube tutorials mapped to learning objectives
- 📝 **Skill Assessment** - Comprehensive MCQ testing system with instant feedback
- 🔒 **Secure & Scalable** - Role-based authentication with bcrypt encryption
- 💻 **100% Offline** - No external APIs required, works completely standalone

---

## ✨ Key Features

### For Learners 👨‍🎓

#### 🗺️ **AI Roadmap Generator**
- Generate personalized learning paths for:
  - **Web Development** (Frontend, Backend, Full-Stack)
  - **Data Science** (Analytics, ML, Deep Learning)
  - **Mobile Development** (iOS, Android, Cross-Platform)
- Three difficulty levels: Beginner, Intermediate, Advanced
- 45 pre-defined, industry-aligned learning steps
- Estimated completion times for each milestone

#### 📚 **Integrated Learning Resources**
- 90+ curated YouTube video tutorials
- Topic-specific learning materials
- Step-by-step guidance with detailed descriptions
- External resource links (documentation, courses, tools)

#### 📝 **Interactive Assessment System**
- Multiple-choice question (MCQ) tests
- Instant scoring and performance feedback
- Detailed answer explanations
- Topic-wise test categorization
- Difficulty-based test selection

#### 📊 **Progress Tracking & Analytics**
- Visual progress bars for roadmap completion
- Comprehensive test history
- Performance trends over time
- Average score calculations
- Personal dashboard with key metrics

### For Administrators 🔧

#### 🎯 **Topic Management**
- Create and organize learning topics
- Categorize by domain and difficulty
- Add detailed descriptions
- Delete outdated content

#### 📝 **Test Creation Suite**
- Build custom MCQ tests
- Add multiple questions per test
- Provide correct answers and explanations
- Set difficulty levels
- Link tests to specific topics

#### 👥 **User Management**
- View all registered users
- Monitor user activity and engagement
- Access user statistics (roadmaps, tests, scores)
- Delete inactive accounts
- Role-based access control

#### 📈 **Analytics Dashboard**
- Platform-wide statistics
- User engagement metrics
- Topic popularity insights
- Test performance analytics
- Real-time activity monitoring

---

## 🔑 Demo Credentials

### Admin Account
```
Username: admin
Password: admin123
```

### Create User Account
Users can self-register through the "Register" tab on the login page.

---

## 🛠️ Tech Stack

### Core Technologies
- **Frontend/Backend**: Streamlit 1.31.0
- **Database**: SQLite (file-based, no server required)
- **Language**: Python 3.8+
- **Authentication**: streamlit-authenticator + bcrypt

### Key Libraries
```
streamlit==1.31.0
streamlit-authenticator==0.2.3
PyYAML==6.0.1
bcrypt==4.1.2
python-dotenv==1.0.0
```

### Architecture Highlights
- **MVC Pattern** - Separation of concerns
- **RESTful Design** - Clean data flow
- **Normalized Database** - 7-table schema
- **Session Management** - Secure state handling
- **Role-Based Access Control** - Admin/User permissions

---

## 📁 Project Structure

```
pathwayai/
│
├── 📄 app.py                          # Main Streamlit application
├── 📄 requirements.txt                # Python dependencies
├── 📄 .env                           # Environment variables
├── 📄 setup.py                       # Automated setup script
├── 📄 README.md                      # This file
│
├── 📂 database/
│   ├── __init__.py                   # Package initializer
│   ├── db_manager.py                 # Database operations & ORM
│   └── pathwayai.db                  # SQLite database (auto-created)
│
├── 📂 pages/
│   ├── __init__.py                   # Package initializer
│   ├── admin_dashboard.py            # Admin: Topics, Users, Tests
│   ├── roadmap_generator.py          # AI roadmap creation engine
│   ├── tests.py                      # Test taking interface
│   ├── test_history.py               # Performance tracking & analytics
│   └── user_dashboard.py             # User roadmap viewing & progress
│
└── 📂 utils/
    ├── __init__.py                   # Package initializer
    ├── auth.py                       # Authentication & authorization
    └── roadmap_ai.py                 # Roadmap generation algorithms
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Method 1: Quick Setup (Recommended)

```bash
# 1. Create project directory
mkdir pathwayai
cd pathwayai

# 2. Run automated setup
python setup.py

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch application
streamlit run app.py
```

### Method 2: Manual Setup

```bash
# 1. Create project structure
mkdir pathwayai
cd pathwayai
mkdir database pages utils

# 2. Create __init__.py files
touch database/__init__.py pages/__init__.py utils/__init__.py

# 3. Copy all code files to respective folders
# (Copy from provided artifacts)

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
echo "DATABASE_PATH=database/pathwayai.db" > .env

# 6. Run application
streamlit run app.py
```

### Method 3: Using Virtual Environment (Best Practice)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
streamlit run app.py
```

### Verification

After installation, open your browser and navigate to:
```
http://localhost:8501
```

You should see the PathwayAI login page.

---

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Database configuration
DATABASE_PATH=database/pathwayai.db

# Optional: API keys (for future enhancements)
# ANTHROPIC_API_KEY=your_api_key_here
# YOUTUBE_API_KEY=your_api_key_here
```

### Application Settings

Edit `app.py` to customize:

```python
# Page configuration
st.set_page_config(
    page_title="PathwayAI",           # Browser tab title
    page_icon="🎓",                    # Favicon
    layout="wide",                     # Layout: "wide" or "centered"
    initial_sidebar_state="expanded"   # Sidebar: "expanded" or "collapsed"
)
```

### Database Settings

Edit `database/db_manager.py`:

```python
class DatabaseManager:
    def __init__(self, db_path="database/pathwayai.db"):
        # Change default database path if needed
```

---

## 📘 Usage Guide

### For Users

#### 1️⃣ **Getting Started**

1. Open PathwayAI in your browser
2. Click "Register" tab
3. Create your account (username, email, password)
4. Login with your credentials

#### 2️⃣ **Generate Your First Roadmap**

1. Navigate to **"Generate Roadmap"** from sidebar
2. Select your **career field**:
   - Web Development
   - Data Science
   - Mobile Development
   - Or enter custom field
3. Choose your **skill level**:
   - Beginner (just starting)
   - Intermediate (have basic knowledge)
   - Advanced (experienced, want mastery)
4. Add **specific interests** (optional)
5. Click **"Generate My Roadmap"**

#### 3️⃣ **Follow Your Learning Path**

1. View generated roadmap with detailed steps
2. Click on each step to see:
   - Detailed description
   - Estimated duration
   - Learning resources
   - YouTube video tutorials
3. Click **"Watch Tutorial"** links to learn
4. Mark steps as complete using checkboxes
5. Track your progress with the progress bar

#### 4️⃣ **Take Skill Assessments**

1. Navigate to **"Take Tests"**
2. Browse available tests by topic
3. Click **"Start Test"** on desired test
4. Answer all questions (use Previous/Next to navigate)
5. Click **"Submit Test"** when finished
6. View instant results with:
   - Score percentage
   - Correct/incorrect answers
   - Detailed explanations

#### 5️⃣ **Track Your Progress**

1. Go to **"Test History"**
2. View all past test results
3. See performance trends
4. Review answer explanations
5. Retake tests to improve scores

#### 6️⃣ **Manage Your Roadmaps**

1. Navigate to **"My Roadmaps"**
2. View all your roadmaps
3. Search and filter roadmaps
4. Track completion percentage
5. Delete completed roadmaps

### For Administrators

#### 1️⃣ **Access Admin Panel**

1. Login with admin credentials
2. Access admin menu from sidebar:
   - Dashboard
   - Topic Management
   - User Management
   - View Tests

#### 2️⃣ **Create Learning Topics**

1. Go to **"Topic Management"**
2. Click **"Add New Topic"** tab
3. Fill in topic details:
   - Name (e.g., "Python Fundamentals")
   - Category (e.g., "Data Science")
   - Description
   - Difficulty level
4. Click **"Create Topic"**

#### 3️⃣ **Build Assessment Tests**

1. Navigate to **"View Tests"**
2. Click **"Create New Test"** tab
3. Select topic from dropdown
4. Enter test details:
   - Title
   - Description
   - Difficulty
   - Number of questions
5. Click **"Create Test Structure"**
6. Add questions one by one:
   - Question text
   - Four options (A, B, C, D)
   - Correct answer
   - Explanation (optional)
7. Click **"Save Question"** for each
8. Click **"Finalize and Create Test"**

#### 4️⃣ **Manage Users**

1. Go to **"User Management"**
2. View all registered users
3. See user statistics:
   - Roadmaps created
   - Tests taken
   - Average score
4. Delete inactive users (cannot delete yourself)

#### 5️⃣ **Monitor Platform**

1. Check **"Dashboard"** for:
   - Total users
   - Total topics
   - Total tests
   - Test attempts
2. View recent activity
3. Monitor platform engagement

---

## 🗄️ Database Schema

PathwayAI uses a normalized SQLite database with 7 tables:

### **1. users**
Stores user account information
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,              -- bcrypt hashed
    role TEXT NOT NULL,                  -- 'admin' or 'user'
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### **2. topics**
Learning topic categories
```sql
CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,                  -- e.g., "Python Basics"
    category TEXT NOT NULL,              -- e.g., "Data Science"
    description TEXT,
    difficulty TEXT,                     -- Beginner/Intermediate/Advanced
    created_by INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
)
```

### **3. roadmaps**
User-generated learning roadmaps
```sql
CREATE TABLE roadmaps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    field TEXT NOT NULL,                 -- Career field
    skill_level TEXT NOT NULL,           -- Beginner/Intermediate/Advanced
    interests TEXT,                      -- User-specific interests
    roadmap_data TEXT NOT NULL,          -- JSON data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
```

### **4. roadmap_steps**
Individual steps within roadmaps
```sql
CREATE TABLE roadmap_steps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roadmap_id INTEGER NOT NULL,
    step_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    resources TEXT,                      -- JSON array
    video_links TEXT,                    -- JSON array of YouTube links
    estimated_duration TEXT,
    completed BOOLEAN DEFAULT 0,
    FOREIGN KEY (roadmap_id) REFERENCES roadmaps(id)
)
```

### **5. tests**
Assessment tests
```sql
CREATE TABLE tests (
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
```

### **6. questions**
MCQ questions for tests
```sql
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL,        -- 'A', 'B', 'C', or 'D'
    explanation TEXT,
    FOREIGN KEY (test_id) REFERENCES tests(id)
)
```

### **7. test_results**
User test performance data
```sql
CREATE TABLE test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    score REAL NOT NULL,                 -- Percentage (0-100)
    total_questions INTEGER NOT NULL,
    correct_answers INTEGER NOT NULL,
    answers_data TEXT,                   -- JSON with detailed answers
    taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (test_id) REFERENCES tests(id)
)
```

### Entity Relationship Diagram

```
users (1) ─────┬───── (n) roadmaps
               │
               ├───── (n) test_results
               │
               └───── (n) topics (created_by)

topics (1) ──────── (n) tests

roadmaps (1) ─────── (n) roadmap_steps

tests (1) ──────┬─── (n) questions
                │
                └─── (n) test_results
```

---

## 📸 Screenshots

### User Interface

```
┌─────────────────────────────────────────────────────────┐
│  🎓 PathwayAI                                     [User] │
├─────────────────────────────────────────────────────────┤
│  Dashboard                                               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │ My Roadmaps  │ │ Tests Taken  │ │ Average Score│   │
│  │      3       │ │      12      │ │    85.5%     │   │
│  └──────────────┘ └──────────────┘ └──────────────┘   │
│                                                          │
│  📚 Recent Roadmaps        📝 Recent Test Results       │
│  • Web Dev - Beginner      • Python Basics - 90%        │
│  • Data Science            • HTML Quiz - 85%            │
└─────────────────────────────────────────────────────────┘
```

### Roadmap Generation

```
┌─────────────────────────────────────────────────────────┐
│  🗺️ Generate Your Learning Roadmap                      │
├─────────────────────────────────────────────────────────┤
│  Career Field: [Web Development ▼]                      │
│  Skill Level:  [Beginner ▼]                             │
│  Interests:    [I want to focus on frontend...]         │
│                                                          │
│  [🚀 Generate My Roadmap]                               │
│                                                          │
│  ──────────────────────────────────────────────────────│
│  🎯 Your Personalized Roadmap                           │
│  Web Development - Beginner Level                       │
│  Estimated Duration: 3 months 2 weeks                   │
│                                                          │
│  📌 Step 1: HTML Fundamentals                           │
│     Description: Learn the basics of HTML...            │
│     Duration: 1-2 weeks                                 │
│     🎥 Watch Tutorial | 🎥 Watch Tutorial               │
│     ☐ Mark as Complete                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🎨 Customization

### Adding Custom Roadmaps

Edit `utils/roadmap_ai.py`:

```python
self.roadmap_templates = {
    "Your New Field": {
        "beginner": [
            {
                "title": "Step Title",
                "description": "Detailed description...",
                "estimated_duration": "2 weeks",
                "resources": ["Resource 1", "Resource 2"],
                "video_links": [
                    "https://www.youtube.com/watch?v=VIDEO_ID_1",
                    "https://www.youtube.com/watch?v=VIDEO_ID_2"
                ]
            },
            # Add more steps...
        ],
        "intermediate": [...],
        "advanced": [...]
    }
}
```

### Custom Styling

Edit CSS in `app.py`:

```python
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
```

### Changing Color Scheme

```python
# Primary colors
PRIMARY_COLOR = "#1f77b4"
SECONDARY_COLOR = "#ff7f0e"
SUCCESS_COLOR = "#2ca02c"
WARNING_COLOR = "#ffa500"
ERROR_COLOR = "#d62728"
```

---

## 🔌 API Reference

### Database Manager Methods

```python
from database.db_manager import DatabaseManager

db = DatabaseManager()

# User operations
db.create_user(username, password_hash, role, email)
db.get_user(username)
db.get_all_users()
db.delete_user(user_id)

# Topic operations
db.create_topic(name, category, description, difficulty, created_by)
db.get_all_topics()
db.get_topics_by_category(category)
db.delete_topic(topic_id)

# Roadmap operations
db.create_roadmap(user_id, title, field, skill_level, interests, roadmap_data)
db.add_roadmap_steps(roadmap_id, steps)
db.get_user_roadmaps(user_id)
db.get_roadmap_steps(roadmap_id)
db.update_step_completion(step_id, completed)

# Test operations
db.create_test(topic_id, title, description, difficulty, created_by)
db.add_question(test_id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation)
db.get_all_tests()
db.get_test_questions(test_id)
db.save_test_result(user_id, test_id, score, total_questions, correct_answers, answers_data)
db.get_user_test_history(user_id)
```

### Authentication Manager Methods

```python
from utils.auth import AuthManager

auth = AuthManager(db)

# Authentication
auth.login(username, password)           # Returns user dict or None
auth.register(username, password, email) # Returns True/False
auth.logout()                           # Clears session
auth.is_authenticated()                 # Returns True/False
auth.is_admin()                        # Returns True/False
auth.require_auth()                    # Redirects if not authenticated
auth.require_admin()                   # Redirects if not admin
```

### Roadmap Generator Methods

```python
from utils.roadmap_ai import RoadmapGenerator

generator = RoadmapGenerator()

# Generate roadmap
roadmap = generator.generate_roadmap(field, skill_level, interests)

# Get available options
fields = generator.get_available_fields()      # Returns list of fields
levels = generator.get_skill_levels()          # Returns ['beginner', 'intermediate', 'advanced']
```

---

## 🌐 Deployment

### Local Deployment

Already running locally! Just use:
```bash
streamlit run app.py
```

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Click "Deploy"
5. Your app will be live at `https://your-app.streamlit.app`

### Heroku Deployment

1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t pathwayai .
docker run -p 8501:8501 pathwayai
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt
```

#### Issue: "Port 8501 already in use"
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

#### Issue: "Database locked"
**Solution:**
```bash
# Close all app instances
# Delete database/pathwayai.db
# Restart the app
```

#### Issue: "bcrypt installation fails on Windows"
**Solution:**
```bash
# Install Microsoft C++ Build Tools
# Or use: pip install --upgrade pip setuptools wheel
pip install bcrypt
```

#### Issue: "Cannot import module 'database'"
**Solution:**
```bash
# Make sure __init__.py exists in all folders
touch database/__init__.py pages/__init__.py utils/__init__.py
```

### Debug Mode

Enable debug logging in `app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Reset Database

```bash
# Backup first (optional)
cp database/pathwayai.db database/pathwayai_backup.db

# Delete database
rm database/pathwayai.db

# Restart app (will recreate database)
streamlit run app.py
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Report Bugs** - Open an issue with detailed description
2. **Suggest Features** - Share your ideas for improvements
3. **Add Content** - Create new roadmaps or test questions
4. **Improve Documentation** - Fix typos, add examples
5. **Code Contributions** - Submit pull requests

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add comments for complex logic
- Write descriptive commit messages
- Test your changes thoroughly
- Update documentation if needed

---

## 🗺️ Roadmap

### Version 2.0 (Planned)

- [ ] Integration with Claude API for dynamic roadmap generation
- [ ] YouTube API for automatic video search
- [ ] Export roadmaps as PDF
- [ ] Email notifications for progress milestones
- [ ] Social features (share roadmaps, follow users)
- [ ] Gamification (badges, streaks, leaderboards)
- [ ] Advanced analytics with charts (using Plotly)
- [ ] Mobile app version (React Native)
- [ ] Multi-language support
- [ ] Certificate generation upon completion

### Version 3.0 (Future)

- [ ] Live coding challenges
- [ ] Mentor-student matching
- [ ] Community forum
- [ ] Video course integration
- [ ] Job board integration
- [ ] Skill endorsements
- [ ] AI-powered personalized recommendations
- [ ] Collaborative learning groups

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 PathwayAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 📞 Contact & Support

### Get Help

- **Documentation**: Check this README and inline code comments
- **Issues**: Open an issue on GitHub
- **Discussions**: Join our community discussions

### Connect

- **GitHub**: [Your GitHub Profile]
- **LinkedIn**: [Your LinkedIn Profile]
- **Email**: your.email@example.com
- **Website**: [Your Portfolio Website]

---

## 🙏 Acknowledgments

### Built With

- [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- [SQLite](https://www.sqlite.org/) - Self-contained SQL database engine
- [bcrypt](https://github.com/pyca/bcrypt/) - Password hashing library
- [Python](https://www.python.org/) - Programming language

### Inspiration

This project was inspired by the need for structured, personalized learning paths in tech education and the desire to make career development more accessible.

### Contributors

Thank you to all contributors who have helped improve PathwayAI!

---

## 📊 Project Statistics

- **Lines of Code**: ~3,500+
- **Files**: 17 Python/Config files
- **Database Tables**: 7
- **Predefined Roadmaps**: 9 (3 fields × 3 levels)
- **Total Learning Steps**: 45
- **YouTube Tutorials**: 90+
- **Features**: 20+ major features
- **Supported Languages**: Python
- **Deployment Options**: 5+ platforms

---

<div align="center">

### ⭐ Star this project if you find it helpful!

**Built with ❤️ using Python and Streamlit**

[⬆ Back to Top](#pathwayai-)

---

**PathwayAI** - Intelligent Career Development Platform

*Learn Smarter, Not Harder* 🚀

</div>