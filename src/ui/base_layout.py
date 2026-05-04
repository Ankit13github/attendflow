import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp{
            background: #5865F2 !important;
        }

        .stApp div[data-testid="stColumn"]{
            background-color:#E0E3FF !important;
            padding:2.5rem !important;
            border-radius:5rem !important;
            border: 1px solid rgba(0,0,0,0.05);
        } 
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp{
            background: #E0E3FF !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit UI */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top:1.5rem !important;
        }

        /* HEADINGS */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom:0rem !important;
            color: black !important;
            
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
            color: #383438 !important;
            letter-spacing: 0.08trem;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
            color: #1a1a1a !important;
        }

        /* ================= BUTTONS ================= */
        button {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
        }

        button[kind="secondary"]{
            background-color: #EB459E !important;
        }

        button[kind="tertiary"]{
            background-color: black !important;
        }

        /* FORCE TEXT + ICON WHITE */
        button, button *, button svg {
            color: white !important;
            fill: white !important;
        }

        button:hover{
            transform: scale(1.05);
        }

        /* ================= SELECT BOX ================= */
        div[data-baseweb="select"] > div {
            background-color: white !important;
            color: black !important;
            border-radius: 10px !important;
        }

        div[data-baseweb="menu"] {
            background-color: white !important;
        }

        div[data-baseweb="menu"] * {
            color: black !important;
        }

        /* ================= INPUTS ================= */
        input, textarea {
            background-color: #2b2d42 !important;
            color: white !important;
            border-radius: 10px !important;
        }

        input::placeholder {
            color: #aaa !important;
        }

        /* ================= LABELS ================= */
        label {
            color: black !important;
        }

        /* ================= DIALOG (MODALS) ================= */
        div[role="dialog"] {
            background-color: #0f172a !important;
            border-radius: 20px !important;
            padding: 20px !important;
        }

        div[role="dialog"] * {
            color: white !important;
        }

        div[role="dialog"] button,
        div[role="dialog"] button * {
            color: white !important;
        }
            
        /* 🎯 Target ONLY those colored stat badges */
        div[data-testid="stMarkdownContainer"] div[style*="rgba(235, 69, 158"] {
            color: black !important;
        }

        /* also fix nested spans/text */
        div[data-testid="stMarkdownContainer"] div[style*="rgba(235, 69, 158"] * {
            color: black !important;
        }
                
        /* 🎯 Toast container */
        div[data-testid="stToast"] {
            background-color: #0f172a !important;   /* dark background */
            color: white !important;
        }

        /* 🎯 Toast text */
        div[data-testid="stToast"] * {
            color: white !important;
        }

        /* 🎯 Toast icon */
        div[data-testid="stToast"] svg {
            fill: white !important;
        }
        div[data-testid="stHeadingWithActionElements"] h1 {
            color: #E0E3FF !important;
        }
        </style>
    """, unsafe_allow_html=True)
