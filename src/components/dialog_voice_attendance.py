import streamlit as st

from src.pipelines.voice_pipeline import process_bulk_audio

from src.database.config import supabase

import pandas as pd


from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime


@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):
    st.write('Record audio of students saying I am present. Then AI will recognize the students')


    audio_data = None

    audio_data = st.audio_input("Record classroom audio")

    if st.button('Analyze Audio', width='stretch', type='primary'):
        with st.spinner('Prcessing Audio data'):
            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this course')
                return
            
            candidates_dict = {}

            for s in enrolled_students or []:
                if not isinstance(s, dict):
                    continue

                student = s.get('students')
                if not isinstance(student, dict):
                    continue

                student_id = student.get('student_id')
                voice_emb = student.get('voice_embedding')

                if student_id is not None and voice_emb:
                    candidates_dict[student_id] = voice_emb
            

            if not candidates_dict:
                st.error('No enrolled students have voice profiles registerd')
                return
            if audio_data is None:
                st.warning("Please record audio first")
                return
            
            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log  = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


            for node in enrolled_students:
                if not isinstance(node, dict):
                    continue

                student = node.get('students')
                if not isinstance(student, dict):
                    continue
                
                student_id = student.get('student_id')
                name = student.get('name')

                if student_id is None:
                    continue

                score  = detected_scores.get(student_id, 0.0)
                is_present= score > 0

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": score if is_present else "-",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_log.append({
                    'student_id': student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)