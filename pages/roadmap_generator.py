import streamlit as st
from utils.roadmap_ai import RoadmapGenerator
import json

def show(db, auth):
    auth.require_auth()
    
    st.title("🗺️ Generate Your Learning Roadmap")
    st.write("Create a personalized learning path based on your interests and goals.")
    
    # Initialize roadmap generator
    generator = RoadmapGenerator()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Tell us about your goals")
        
        # Field selection
        available_fields = generator.get_available_fields()
        available_fields.append("Other (Specify)")
        
        field = st.selectbox(
            "Select your career field",
            available_fields,
            help="Choose the field you want to learn"
        )
        
        if field == "Other (Specify)":
            field = st.text_input("Enter your career field", placeholder="e.g., Digital Marketing, Blockchain")
        
        # Skill level
        skill_levels = generator.get_skill_levels()
        skill_level = st.selectbox(
            "What's your current skill level?",
            skill_levels,
            format_func=lambda x: x.capitalize(),
            help="Be honest about your current level"
        )
        
        # Interests
        interests = st.text_area(
            "What are your specific interests? (Optional)",
            placeholder="e.g., I'm interested in AI, want to focus on backend development, prefer video tutorials",
            help="This helps us customize your roadmap"
        )
        
        # Generate button
        if st.button("🚀 Generate My Roadmap", type="primary"):
            if field and skill_level:
                with st.spinner("Creating your personalized roadmap..."):
                    roadmap = generator.generate_roadmap(field, skill_level, interests)
                    
                    # Save to database
                    roadmap_id = db.create_roadmap(
                        user_id=st.session_state.user['id'],
                        title=roadmap['title'],
                        field=roadmap['field'],
                        skill_level=roadmap['skill_level'],
                        interests=interests or "",
                        roadmap_data=roadmap
                    )
                    
                    # Add steps
                    db.add_roadmap_steps(roadmap_id, roadmap['steps'])
                    
                    st.session_state.generated_roadmap = roadmap
                    st.session_state.generated_roadmap_id = roadmap_id
                    st.success("✅ Roadmap generated successfully!")
                    st.rerun()
            else:
                st.warning("Please fill in all required fields")
    
    with col2:
        st.subheader("📋 Quick Tips")
        st.info("""
        **How to choose your level:**
        
        - **Beginner**: Just starting out
        - **Intermediate**: Have basic knowledge
        - **Advanced**: Experienced, want to master
        
        **Pro Tips:**
        - Be specific about your interests
        - Start with beginner if unsure
        - You can generate multiple roadmaps
        """)
    
    # Display generated roadmap
    if 'generated_roadmap' in st.session_state and st.session_state.generated_roadmap:
        st.markdown("---")
        display_roadmap(st.session_state.generated_roadmap, st.session_state.generated_roadmap_id, db)

def display_roadmap(roadmap, roadmap_id, db):
    st.header("🎯 Your Personalized Roadmap")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader(roadmap['title'])
    
    with col2:
        st.metric("Estimated Duration", roadmap.get('total_duration', 'N/A'))
    
    st.write(f"**Field:** {roadmap['field']}")
    st.write(f"**Skill Level:** {roadmap['skill_level'].capitalize()}")
    
    st.markdown("---")
    
    # Display steps
    for i, step in enumerate(roadmap['steps'], 1):
        with st.expander(f"📌 Step {i}: {step['title']}", expanded=(i == 1)):
            st.write(f"**Description:**")
            st.write(step['description'])
            
            st.write(f"**⏱️ Estimated Duration:** {step.get('estimated_duration', 'N/A')}")
            
            # Resources
            if step.get('resources'):
                st.write("**📚 Resources:**")
                for resource in step['resources']:
                    st.write(f"- {resource}")
            
            # Video links
            if step.get('video_links'):
                st.write("**🎥 Video Tutorials:**")
                for video_link in step['video_links']:
                    st.markdown(f"[▶️ Watch Tutorial]({video_link})")
            
            # Completion tracking
            steps = db.get_roadmap_steps(roadmap_id)
            if i <= len(steps):
                step_id = steps[i-1][0]
                completed = steps[i-1][8]
                
                col1, col2 = st.columns([3, 1])
                with col2:
                    if st.checkbox("Mark as Complete", value=bool(completed), key=f"complete_{step_id}"):
                        db.update_step_completion(step_id, 1)
                        st.success("✅ Marked as complete!")
                    else:
                        if completed:
                            db.update_step_completion(step_id, 0)
    
    st.markdown("---")
    
    # Progress tracking
    steps = db.get_roadmap_steps(roadmap_id)
    completed_steps = sum(1 for step in steps if step[8])
    total_steps = len(steps)
    progress = (completed_steps / total_steps * 100) if total_steps > 0 else 0
    
    st.subheader("📊 Your Progress")
    st.progress(progress / 100)
    st.write(f"Completed {completed_steps} out of {total_steps} steps ({progress:.1f}%)")
    
    if completed_steps == total_steps:
        st.balloons()
        st.success("🎉 Congratulations! You've completed this roadmap!")