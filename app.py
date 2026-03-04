import streamlit as st
from database.db_manager import DatabaseManager
from utils.auth import AuthManager

# Page configuration
st.set_page_config(
    page_title="PathwayAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database and auth
@st.cache_resource
def init_app():
    db = DatabaseManager()
    auth = AuthManager(db)
    return db, auth

db, auth = init_app()

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
def show_sidebar():
    with st.sidebar:
        st.title("🎓 PathwayAI")
        
        if st.session_state.user:
            st.success(f"Welcome, {st.session_state.user['username']}!")
            st.info(f"Role: {st.session_state.user['role'].capitalize()}")
            
            st.markdown("---")
            
            # Navigation based on role
            if st.session_state.user['role'] == 'admin':
                st.subheader("Admin Menu")
                page = st.radio(
                    "Navigate to:",
                    ["Dashboard", "Topic Management", "User Management", "View Tests", "Profile"],
                    key="admin_nav"
                )
            else:
                st.subheader("User Menu")
                page = st.radio(
                    "Navigate to:",
                    ["Dashboard", "Generate Roadmap", "My Roadmaps", "Take Tests", "Test History", "Profile"],
                    key="user_nav"
                )
            
            st.markdown("---")
            
            if st.button("🚪 Logout"):
                auth.logout()
                st.rerun()
            
            return page
        else:
            st.info("Please login to continue")
            return None

# Login Page
def show_login():
    st.title("🎓 PathwayAI - Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            st.subheader("Login to Your Account")
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")
                
                if submit:
                    if username and password:
                        user = auth.login(username, password)
                        if user:
                            st.session_state.user = user
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error("Invalid username or password")
                    else:
                        st.warning("Please fill in all fields")
        
        with tab2:
            st.subheader("Create New Account")
            with st.form("register_form"):
                new_username = st.text_input("Username", key="reg_username")
                new_email = st.text_input("Email", key="reg_email")
                new_password = st.text_input("Password", type="password", key="reg_password")
                confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")
                submit_reg = st.form_submit_button("Register")
                
                if submit_reg:
                    if new_username and new_password and new_email:
                        if new_password == confirm_password:
                            if auth.register(new_username, new_password, new_email):
                                st.success("Registration successful! Please login.")
                            else:
                                st.error("Username already exists")
                        else:
                            st.error("Passwords do not match")
                    else:
                        st.warning("Please fill in all fields")
        
        st.markdown("---")
        st.info("**Demo Credentials:**\n\nAdmin: admin / admin123")

# Dashboard Pages
def show_user_dashboard():
    st.title("👋 Welcome to Your Dashboard")
    
    user_id = st.session_state.user['id']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        roadmaps = db.get_user_roadmaps(user_id)
        st.metric("My Roadmaps", len(roadmaps))
    
    with col2:
        test_history = db.get_user_test_history(user_id)
        st.metric("Tests Taken", len(test_history))
    
    with col3:
        if test_history:
            avg_score = sum([r[3] for r in test_history]) / len(test_history)
            st.metric("Average Score", f"{avg_score:.1f}%")
        else:
            st.metric("Average Score", "N/A")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Recent Roadmaps")
        if roadmaps:
            for roadmap in roadmaps[:5]:
                with st.expander(f"{roadmap[2]} - {roadmap[3]}"):
                    st.write(f"**Created:** {roadmap[6]}")
                    st.write(f"**Skill Level:** {roadmap[4]}")
                    if st.button("View Details", key=f"view_roadmap_{roadmap[0]}"):
                        st.session_state.selected_roadmap = roadmap[0]
                        st.session_state.page = "My Roadmaps"
                        st.rerun()
        else:
            st.info("No roadmaps yet. Generate your first roadmap!")
    
    with col2:
        st.subheader("📝 Recent Test Results")
        if test_history:
            for result in test_history[:5]:
                with st.expander(f"{result[7]} - {result[3]:.1f}%"):
                    st.write(f"**Topic:** {result[8]}")
                    st.write(f"**Score:** {result[5]}/{result[4]} correct")
                    st.write(f"**Date:** {result[6]}")
        else:
            st.info("No tests taken yet. Start with a test!")

def show_admin_dashboard():
    st.title("🔧 Admin Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        users = db.get_all_users()
        st.metric("Total Users", len(users))
    
    with col2:
        topics = db.get_all_topics()
        st.metric("Total Topics", len(topics))
    
    with col3:
        tests = db.get_all_tests()
        st.metric("Total Tests", len(tests))
    
    with col4:
        # Get all test results
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM test_results")
        total_attempts = cursor.fetchone()[0]
        conn.close()
        st.metric("Test Attempts", total_attempts)
    
    st.markdown("---")
    
    st.subheader("📊 Quick Stats")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Recent Users**")
        recent_users = users[-5:]
        for user in recent_users:
            st.text(f"• {user[1]} ({user[2]}) - {user[4]}")
    
    with col2:
        st.write("**Recent Topics**")
        recent_topics = topics[-5:] if topics else []
        for topic in recent_topics:
            st.text(f"• {topic[1]} ({topic[2]})")

# Profile Page
def show_profile():
    st.title("👤 My Profile")
    
    user = st.session_state.user
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Account Information")
        st.write(f"**Username:** {user['username']}")
        st.write(f"**Email:** {user.get('email', 'Not provided')}")
        st.write(f"**Role:** {user['role'].capitalize()}")
    
    with col2:
        st.subheader("Update Profile")
        st.info("Profile update functionality coming soon!")

# Main App Logic
def main():
    if not st.session_state.user:
        show_login()
    else:
        page = show_sidebar()
        
        if page == "Dashboard":
            if st.session_state.user['role'] == 'admin':
                show_admin_dashboard()
            else:
                show_user_dashboard()
        
        elif page == "Profile":
            show_profile()
        
        # Import and show other pages (we'll create these next)
        elif page == "Generate Roadmap":
            from pages import roadmap_generator
            roadmap_generator.show(db, auth)
        
        elif page == "My Roadmaps":
            from pages import user_dashboard
            user_dashboard.show_roadmaps(db, auth)
        
        elif page == "Take Tests":
            from pages import tests
            tests.show_test_selection(db, auth)
        
        elif page == "Test History":
            from pages import test_history
            test_history.show(db, auth)
        
        elif page == "Topic Management":
            from pages import admin_dashboard
            admin_dashboard.show_topic_management(db, auth)
        
        elif page == "User Management":
            from pages import admin_dashboard
            admin_dashboard.show_user_management(db, auth)
        
        elif page == "View Tests":
            from pages import admin_dashboard
            admin_dashboard.show_test_management(db, auth)

if __name__ == "__main__":
    main()

    #python -m streamlit run app.py
    