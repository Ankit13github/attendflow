import streamlit as st


def footer_dashboard():
    logo_url = ""
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by Ankit Malviya </p>  
         <!-- <img src='{logo_url}' style='max-height:25px' /> -->
        </div>
                
                """, unsafe_allow_html=True)
    

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
<style>
.custom-footer {{
    margin-top: 3rem;
    padding: 20px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1e293b, #020617);
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}}

.custom-footer img {{

    height: 30px;
    margin-bottom: 8px;
}}

.footer-header {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}}

/* adjust logo size slightly */
.footer-header img {{
    height: 35px;
}}  

.footer-title {{
    color: white;
    font-weight: 600;
    font-size: 1.7rem;
    font-size: 1.4rem;
    letter-spacing: 0.5px;
}}


.footer-text {{
    color: #e2e8f0;
    font-size: 0.95rem;
}}
.footer-icons {{
    display: flex;
    gap: 16px;
    font-size: 1.3rem;
    align-items: center;
    justify-content: center;

}}

.footer-icons a {{
    color: white;
    text-decoration: none;
    transition: transform 0.2s ease, opacity 0.2s ease;
}}

.footer-icons a:hover {{
    transform: scale(1.2);
    opacity: 0.8;
}}

.footer-bottom {{
    color: #94a3b8;
    font-size: 0.8rem;
    margin-top: 6px;
}}
</style>

<div class="custom-footer">
<div class="footer-header">
    <img src="{logo_url}" />
    <div class="footer-title">Attend Flow</div>
</div>
<div class="footer-text">Made with ❤️ by Ankit Malviya</div>
<div class="footer-icons">
<a href="https://github.com/Ankit13github" target="_blank">🐙</a>
<a href="https://www.linkedin.com/in/ankit-malviya13" target="_blank">💼</a>
<a href="mailto:malviyaankit13127@gmail.com">📧</a>
</div>
<div class="footer-bottom">© 2026 Attend Flow</div>
</div>
""",
        unsafe_allow_html=True
    )