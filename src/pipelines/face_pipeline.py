

#import dlib  # type: ignore
import numpy as np
#import face_recognition_models
#from sklearn.svm import SVC
import streamlit as st
from typing import List, Dict, Any

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()  

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )  

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )  

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []

    raw_students = get_all_students() or []
    student_db: List[Dict[str, Any]] = [
        s for s in raw_students if isinstance(s,dict) 
    ]

    for student in student_db:
        embedding = student.get('face_embedding')
        student_id = student.get('student_id')

        if embedding and student_id is not None:
            X.append(np.array(embedding))
            y.append(student_id)

    if len(X) == 0:
        return None
    
    X = np.array(X)
    y = np.array(y)

    if len(set(y)) == 1:
        return {'single_class': int(y[0]), 'X': X, 'y': y}
    
    clf = SVC(kernel='linear', probability=True, class_weight='balanced')
    clf.fit(X, y)

    return {'clf': clf, 'X':X, "y":y}


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}


    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    X_train = model_data['X']
    y_train = model_data['y']

    if 'single_class' in model_data:
        single_id = model_data['single_class']

        for encoding in encodings:
            student_embedding = X_train[0]
            score = np.linalg.norm(student_embedding - encoding)
            
            if score <=0.6:
                detected_student[single_id] = True
        return detected_student, [single_id], len(encodings)
    
    
    clf = model_data['clf']
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        predicted_id = int(clf.predict([encoding])[0])

        indices = np.where(y_train == predicted_id)[0]
        student_embedding = X_train[indices[0]] 

        score = np.linalg.norm(student_embedding - encoding)

        if score <= 0.6:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)
