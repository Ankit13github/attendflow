import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

import time


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject Code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()

            if res.data:
                subject = res.data[0]

                if not isinstance(subject, dict):
                    st.error("Invalid subject data")
                    return
                
                subject_id_val = subject.get('subject_id')
                subject_name = subject.get('name')

                student_data = st.session_state.get('student_data', {})
                student_id = student_data.get('student_id')

                check = supabase.table('subject_students').select('*').eq('subject_id', subject_id_val).eq('student_id', student_id).execute()

                if check.data:
                    st.warning('You are already enrolled in this program')
                else:
                    enroll_student_to_subject(student_id, subject_id_val)
                    st.success(f'Succesfully enrolled in {subject_name}!')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning('Please enter a subject code') 