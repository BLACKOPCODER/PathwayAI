import streamlit as st
import json

def show_roadmaps(db, auth):
    auth.require_auth()
    
    st.title("📚 My Learning Roadmaps")
    
    user_id = st.session_state.user['id']
    roadmaps = db.get_user_roadmaps(user_id)
    
    if not roadmaps:
        st.info("You haven't created any roadmaps yet. Generate your first roadmap from the menu!")
        if st.button("Generate Roadmap"):
            st.session_state.page = "Generate Roadmap"
            st.rerun()
        return
    
    st.write(f"You have {len(roadmaps)} roadmap(s)")
    
    # Filter options
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search = st.text_input("🔍 Search roadmaps", placeholder="Search by title or field")
    
    with col2:
        sort_by = st.selectbox("Sort by", ["Newest First", "Oldest First", "Field"])
    
    # Sort roadmaps
    if sort_by == "Newest First":
        roadmaps = sorted(roadmaps, key=lambda x: x[6], reverse=True)
    elif sort_by == "Oldest First":
        roadmaps = sorted(roadmaps, key=lambda x: x[6])
    elif sort_by == "Field":
        roadmaps = sorted(roadmaps, key=lambda x: x[3])
    
    # Filter by search
    if search:
        roadmaps = [r for r in roadmaps if search.lower() in r[2].lower() or search.lower() in r[3].lower()]
    
    st.markdown("---")
    
    # Display roadmaps
    for roadmap in roadmaps:
        roadmap_id = roadmap[0]
        title = roadmap[2]
        field = roadmap[3]
        skill_level = roadmap[4]
        created_at = roadmap[6]
        
        # Get progress
        steps = db.get_roadmap_steps(roadmap_id)
        completed_steps = sum(1 for step in steps if step[8])
        total_steps = len(steps)
        progress = (completed_steps / total_steps * 100) if total_steps > 0 else 0
        
        with st.expander(f"🎯 {title}", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write(f"**Field:** {field}")
                st.write(f"**Level:** {skill_level.capitalize()}")
            
            with col2:
                st.write(f"**Created:** {created_at[:10]}")
                st.write(f"**Total Steps:** {total_steps}")
            
            with col3:
                st.metric("Progress", f"{progress:.0f}%")
            
            st.progress(progress / 100)
            
            # Display steps
            st.markdown("### 📋 Learning Steps")
            
            for step in steps:
                step_id = step[0]
                step_number = step[2]
                step_title = step[3]
                step_description = step[4]
                resources = json.loads(step[5]) if step[5] else []
                video_links = json.loads(step[6]) if step[6] else []
                estimated_duration = step[7]
                completed = step[8]
                
                # Step container
                step_container = st.container()
                
                with step_container:
                    col1, col2 = st.columns([5, 1])
                    
                    with col1:
                        if completed:
                            st.write(f"✅ **{step_number}. {step_title}** _(Completed)_")
                        else:
                            st.write(f"⭐ **{step_number}. {step_title}**")
                        
                        with st.expander("View Details"):
                            st.write(step_description)
                            st.write(f"**Duration:** {estimated_duration}")
                            
                            if resources:
                                st.write("**Resources:**")
                                for resource in resources:
                                    st.write(f"- {resource}")
                            
                            if video_links:
                                st.write("**Video Tutorials:**")
                                for link in video_links:
                                    st.markdown(f"[▶️ Watch Tutorial]({link})")
                    
                    with col2:
                        if st.checkbox("Done", value=bool(completed), key=f"step_{step_id}"):
                            db.update_step_completion(step_id, 1)
                            st.rerun()
                        else:
                            if completed:
                                db.update_step_completion(step_id, 0)
                                st.rerun()
            
            st.markdown("---")
            
            # Delete roadmap option
            if st.button("🗑️ Delete Roadmap", key=f"delete_{roadmap_id}"):
                if st.session_state.get(f'confirm_delete_{roadmap_id}'):
                    # Delete roadmap and its steps
                    conn = db.get_connection()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM roadmap_steps WHERE roadmap_id = ?", (roadmap_id,))
                    cursor.execute("DELETE FROM roadmaps WHERE id = ?", (roadmap_id,))
                    conn.commit()
                    conn.close()
                    st.success("Roadmap deleted successfully!")
                    st.rerun()
                else:
                    st.session_state[f'confirm_delete_{roadmap_id}'] = True
                    st.warning("Click again to confirm deletion")