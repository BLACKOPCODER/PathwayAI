import streamlit as st
import json
from datetime import datetime

def show(db, auth):
    auth.require_auth()
    
    st.title("📊 My Test History")
    
    user_id = st.session_state.user['id']
    test_history = db.get_user_test_history(user_id)
    
    if not test_history:
        st.info("You haven't taken any tests yet. Start with your first test!")
        if st.button("Take a Test"):
            st.session_state.page = "Take Tests"
            st.rerun()
        return
    
    # Statistics
    total_tests = len(test_history)
    avg_score = sum([r[3] for r in test_history]) / total_tests
    best_score = max([r[3] for r in test_history])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tests Taken", total_tests)
    
    with col2:
        st.metric("Average Score", f"{avg_score:.1f}%")
    
    with col3:
        st.metric("Best Score", f"{best_score:.1f}%")
    
    st.markdown("---")
    
    # Filters
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search = st.text_input("🔍 Search tests", placeholder="Search by test name or topic")
    
    with col2:
        sort_by = st.selectbox("Sort by", ["Newest First", "Oldest First", "Highest Score", "Lowest Score"])
    
    # Sort results
    if sort_by == "Newest First":
        test_history = sorted(test_history, key=lambda x: x[6], reverse=True)
    elif sort_by == "Oldest First":
        test_history = sorted(test_history, key=lambda x: x[6])
    elif sort_by == "Highest Score":
        test_history = sorted(test_history, key=lambda x: x[3], reverse=True)
    elif sort_by == "Lowest Score":
        test_history = sorted(test_history, key=lambda x: x[3])
    
    # Filter by search
    if search:
        test_history = [t for t in test_history if 
                       search.lower() in t[7].lower() or 
                       search.lower() in t[8].lower()]
    
    st.markdown("---")
    
    # Display test history
    for result in test_history:
        result_id = result[0]
        test_id = result[2]
        score = result[3]
        total_questions = result[4]
        correct_answers = result[5]
        taken_at = result[6]
        test_title = result[7]
        topic_name = result[8]
        answers_data = json.loads(result[9]) if result[9] else []
        
        # Color coding based on score
        if score >= 80:
            score_color = "🟢"
            score_label = "Excellent"
        elif score >= 60:
            score_color = "🟡"
            score_label = "Good"
        else:
            score_color = "🔴"
            score_label = "Needs Improvement"
        
        with st.expander(f"{score_color} {test_title} - {score:.1f}%", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write(f"**Topic:** {topic_name}")
                st.write(f"**Date:** {taken_at[:16]}")
            
            with col2:
                st.write(f"**Score:** {score:.1f}%")
                st.write(f"**Performance:** {score_label}")
            
            with col3:
                st.write(f"**Correct:** {correct_answers}/{total_questions}")
                percentage = (correct_answers / total_questions * 100)
                st.progress(percentage / 100)
            
            st.markdown("---")
            
            # Show detailed answers
            st.subheader("📋 Answer Review")
            
            if answers_data:
                for i, answer in enumerate(answers_data, 1):
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.write(f"**Q{i}. {answer.get('question', 'N/A')}**")
                        
                        with col2:
                            if answer.get('is_correct'):
                                st.success("✅")
                            else:
                                st.error("❌")
                        
                        with st.expander("View Details"):
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.write(f"**Your Answer:** {answer.get('user_answer', 'N/A')}")
                            
                            with col2:
                                st.write(f"**Correct Answer:** {answer.get('correct_answer', 'N/A')}")
                            
                            if answer.get('explanation'):
                                st.info(f"**Explanation:** {answer['explanation']}")
                        
                        st.markdown("---")
            
            # Retake option
            if st.button("🔄 Retake Test", key=f"retake_{result_id}"):
                st.session_state.current_test_id = test_id
                st.session_state.test_started = True
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.page = "Take Tests"
                st.rerun()
    
    st.markdown("---")
    
    # Performance chart (simple text-based for now)
    st.subheader("📈 Performance Over Time")
    
    if len(test_history) >= 2:
        recent_tests = test_history[:10]
        
        st.write("Recent Test Scores:")
        for result in recent_tests:
            score = result[3]
            test_title = result[7]
            taken_at = result[6][:10]
            
            bar_length = int(score / 5)
            bar = "█" * bar_length
            
            st.text(f"{taken_at} | {test_title[:30]:<30} | {bar} {score:.0f}%")
    else:
        st.info("Take more tests to see your performance trend!")