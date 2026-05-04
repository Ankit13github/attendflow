# 🚀 Attend Flow — AI-Based Attendance System

[![Live Demo](https://img.shields.io/badge/Attend%20Flow-Live%20Demo-5865F2?style=for-the-badge)](https://attend-flow.streamlit.app)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/Machine%20Learning-SVM-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> ⚡ Try the app live — no setup required.

---

## 📌 Overview

**Attend Flow** is an intelligent attendance system that uses **Face Recognition and Voice Recognition** to automate classroom attendance. It removes manual effort and provides a seamless experience for both teachers and students.

---

## ✨ Features

### 👨‍🏫 Teacher Panel

* Create and manage subjects
* Share subject codes for enrollment
* Take attendance using:

  * 📸 Face Recognition (image-based)
  * 🎤 Voice Recognition (audio-based)
* View attendance records and insights

---

### 🎓 Student Panel

* Register with face and optional voice data
* Join classes using subject code
* Get marked present automatically
* View attendance status

---

## 🧠 AI / ML Pipeline

* Face embeddings using **dlib**
* Voice embeddings for speaker recognition
* Classification using **SVM (Scikit-learn)**
* Similarity matching using distance metrics

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** Supabase
* **ML Libraries:** dlib, scikit-learn, NumPy
* **Image Processing:** Pillow

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/attend-flow.git
cd attend-flow

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

## 🗂️ Project Structure

```text
src/
│
├── database/
│   ├── db.py
│   ├── config.py
│
├── pipelines/
│   ├── face_pipeline.py
│   ├── voice_pipeline.py
│
├── screens/
│   ├── teacher_screen.py
│   ├── student_screen.py
│   ├── home_screen.py
│
├── components/
│   ├── dialod_add_photo.py
│   ├── dialod_add_attendance.py
│   ├── dialod_auto_enroll.py
│   ├── dialod_create_subject.py
│   ├── dialod_enroll.py
│   ├── dialog_share_subject.py
│   ├── dialod_voice_attendance.py
│   ├── footer.py
│   ├── header.py
│   ├── subject_card.py
│
├── teacher_screen.py
│   ├── student_screen.py
│   ├── home_screen.py
├── ui/
│   ├── base_layout.py
│   
│
app.py
requirements.txt
README.md
.gitignore

```

---

## 🚧 Challenges Solved

* dlib installation and compatibility issues
* Supabase Row Level Security (RLS) configuration
* Handling ML edge cases (single-class training issue)
* Maintaining consistent UI with Streamlit CSS

---

## 🔮 Future Improvements

* Real-time video-based attendance
* Mobile-friendly UI
* Improved voice recognition accuracy
* Advanced analytics dashboard

---

## 👨‍💻 Author

**Your Name**
GitHub: https://github.com/Ankit13github
LinkedIn: https://linkedin.com/in/ankit-malviya113

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
