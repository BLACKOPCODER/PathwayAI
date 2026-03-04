import streamlit as st
import json

def show_test_selection(db, auth):
    auth.require_auth()
    
    st.title("📝 Take a Test")
    
    tests = db.get_all_tests()
    
    if not tests:
        st.info("No tests available yet. Please check back later!")
        return
    
    st.write(f"Available Tests: {len(tests)}")
    
    # Group tests by topic
    topics_dict = {}
    for test in tests:
        topic_name = test[7]
        if topic_name not in topics_dict:
            topics_dict[topic_name] = []
        topics_dict[topic_name].append(test)
    
    # Display tests by topic
    for topic_name, topic_tests in topics_dict.items():
        st.subheader(f"📚 {topic_name}")
        
        for test in topic_tests:
            test_id = test[0]
            title = test[2]
            description = test[3]
            difficulty = test[4]
            
            # Get number of questions
            questions = db.get_test_questions(test_id)
            num_questions = len(questions)
            
            with st.expander(f"{title} ({difficulty})"):
                st.write(f"**Description:** {description}")
                st.write(f"**Questions:** {num_questions}")
                st.write(f"**Difficulty:** {difficulty}")
                
                if st.button("Start Test", key=f"start_{test_id}"):
                    st.session_state.current_test_id = test_id
                    st.session_state.test_started = True
                    st.session_state.current_question = 0
                    st.session_state.answers = {}
                    st.rerun()
    
    # Show active test
    if st.session_state.get('test_started'):
        show_test(db, auth)

def show_test(db, auth):
    test_id = st.session_state.current_test_id
    questions = db.get_test_questions(test_id)
    
    if not questions:
        st.error("This test has no questions")
        return
    
    # Get test info
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.*, tp.name as topic_name 
        FROM tests t 
        JOIN topics tp ON t.topic_id = tp.id
        WHERE t.id = ?
    ''', (test_id,))
    test_info = cursor.fetchone()
    conn.close()
    
    st.markdown("---")
    st.title(f"📝 {test_info[2]}")
    
    current_q = st.session_state.current_question
    total_questions = len(questions)
    
    # Progress bar
    progress = (current_q + 1) / total_questions
    st.progress(progress)
    st.write(f"Question {current_q + 1} of {total_questions}")
    
    # Display current question
    question = questions[current_q]
    q_id = question[0]
    q_text = question[2]
    option_a = question[3]
    option_b = question[4]
    option_c = question[5]
    option_d = question[6]
    
    st.markdown("---")
    st.subheader(f"Q{current_q + 1}. {q_text}")
    
    # Answer options
    answer = st.radio(
        "Select your answer:",
        ["A", "B", "C", "D"],
        format_func=lambda x: f"{x}. " + [option_a, option_b, option_c, option_d][ord(x) - ord('A')],
        key=f"question_{q_id}"
    )
    
    # Store answer
    if answer:
        st.session_state.answers[q_id] = answer
    
    st.markdown("---")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if current_q > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col3:
        if current_q < total_questions - 1:
            if st.button("Next ➡️"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("Submit Test 🎯", type="primary"):
                submit_test(db, auth, test_id, questions)

def submit_test(db, auth, test_id, questions):
    user_id = st.session_state.user['id']
    answers = st.session_state.answers
    
    # Calculate score
    correct_answers = 0
    total_questions = len(questions)
    answers_data = []
    
    for question in questions:
        q_id = question[0]
        correct_answer = question[7]
        user_answer = answers.get(q_id, "")
        is_correct = user_answer == correct_answer
        
        if is_correct:
            correct_answers += 1
        
        answers_data.append({
            "question_id": q_id,
            "question": question[2],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "explanation": question[8]
        })
    
    score = (correct_answers / total_questions) * 100
    
    # Save result
    db.save_test_result(
        user_id=user_id,
        test_id=test_id,
        score=score,
        total_questions=total_questions,
        correct_answers=correct_answers,
        answers_data=answers_data
    )
    
    # Show results
    st.session_state.test_completed = True
    st.session_state.test_score = score
    st.session_state.test_correct = correct_answers
    st.session_state.test_total = total_questions
    st.session_state.test_answers = answers_data
    
    # Clear test state
    st.session_state.test_started = False
    st.session_state.current_test_id = None
    st.session_state.current_question = 0
    st.session_state.answers = {}
    
    st.rerun()

def show_test_results():
    if not st.session_state.get('test_completed'):
        return
    
    st.title("🎉 Test Results")
    
    score = st.session_state.test_score
    correct = st.session_state.test_correct
    total = st.session_state.test_total
    answers_data = st.session_state.test_answers
    
    # Score display
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Score", f"{score:.1f}%")
    
    with col2:
        st.metric("Correct Answers", f"{correct}/{total}")
    
    with col3:
        if score >= 80:
            st.success("Excellent! 🌟")
        elif score >= 60:
            st.info("Good Job! 👍")
        else:
            st.warning("Keep Learning! 📚")
    
    st.markdown("---")
    
    # Detailed answers
    st.subheader("📋 Answer Review")
    
    for i, answer in enumerate(answers_data, 1):
        with st.expander(f"Q{i}. {answer['question']}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Your Answer:** {answer['user_answer']}")
            
            with col2:
                st.write(f"**Correct Answer:** {answer['correct_answer']}")
            
            if answer['is_correct']:
                st.success("✅ Correct!")
            else:
                st.error("❌ Incorrect")
            
            if answer['explanation']:
                st.info(f"**Explanation:** {answer['explanation']}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Take Another Test"):
            st.session_state.test_completed = False
            st.rerun()
    
    with col2:
        if st.button("View Test History"):
            st.session_state.page = "Test History"
            st.rerun()

# Main function
def show_test_selection(db, auth):
    if st.session_state.get('test_completed'):
        show_test_results()
    elif st.session_state.get('test_started'):
        show_test(db, auth)
    else:
        auth.require_auth()
        
        st.title("📝 Take a Test")
        
        tests = db.get_all_tests()
        
        if not tests:
            st.info("No tests available yet. Please check back later!")
            return
        
        st.write(f"Available Tests: {len(tests)}")
        
        # Group tests by topic
        topics_dict = {}
        for test in tests:
            topic_name = test[7]
            if topic_name not in topics_dict:
                topics_dict[topic_name] = []
            topics_dict[topic_name].append(test)
        
        # Display tests by topic
        for topic_name, topic_tests in topics_dict.items():
            st.subheader(f"📚 {topic_name}")
            
            for test in topic_tests:
                test_id = test[0]
                title = test[2]
                description = test[3]
                difficulty = test[4]
                
                # Get number of questions
                questions = db.get_test_questions(test_id)
                num_questions = len(questions)
                
                with st.expander(f"{title} ({difficulty})"):
                    st.write(f"**Description:** {description}")
                    st.write(f"**Questions:** {num_questions}")
                    st.write(f"**Difficulty:** {difficulty}")
                    
                    if st.button("Start Test", key=f"start_{test_id}"):
                        st.session_state.current_test_id = test_id
                        st.session_state.test_started = True
                        st.session_state.current_question = 0
                        st.session_state.answers = {}
                        st.rerun()
