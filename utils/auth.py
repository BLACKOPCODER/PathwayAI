import bcrypt
import streamlit as st
from database.db_manager import DatabaseManager

class AuthManager:
    def __init__(self, db_manager):
        self.db = db_manager
    
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    def login(self, username, password):
        user = self.db.get_user(username)
        if user and self.verify_password(password, user[2]):  # user[2] is password
            return {
                'id': user[0],
                'username': user[1],
                'role': user[3],
                'email': user[4]
            }
        return None
    
    def register(self, username, password, email=None, role='user'):
        password_hash = self.hash_password(password)
        return self.db.create_user(username, password_hash, role, email)
    
    def logout(self):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    
    def is_authenticated(self):
        return 'user' in st.session_state and st.session_state.user is not None
    
    def is_admin(self):
        return self.is_authenticated() and st.session_state.user['role'] == 'admin'
    
    def require_auth(self):
        if not self.is_authenticated():
            st.warning("Please login to access this page")
            st.stop()
    
    def require_admin(self):
        if not self.is_admin():
            st.error("Admin access required")
            st.stop()