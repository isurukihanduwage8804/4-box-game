import streamlit as st
import random

# පිටුවේ සැකසුම්
st.set_page_config(page_title="Lassana Education App", layout="centered")

# --- ලස්සන CSS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 120px;
        border-radius: 20px;
        font-size: 22px;
        background: linear-gradient(145deg, #FF4B4B, #FF8080);
        color: white;
        box-shadow: 5px 5px 15px #d1d1d1;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: translateY(-5px);
        background: linear-gradient(145deg, #FF8080, #FF4B4B);
    }
    .question-style {
        background-color: #f9f9f9;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #FF4B4B;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ප්‍රශ්න 20 කට්ටලය ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"q": "පරිගණකයක ප්‍රධාන දත්ත සැකසුම් ඒකකය කුමක්ද?", "o": ["RAM", "CPU", "ROM", "GPU"], "a": "CPU"},
        {"q": "ශ්‍රී ලංකාවේ වැඩිම උසකින් යුත් කන්ද කුමක්ද?", "o": ["සමනල කන්ද", "පිදුරුතලාගල", "නමුනුකුල", "හන්තාන"], "a": "පිදුරුතලාගල"},
        {"q": "ලෝකයේ විශාලතම සත්වයා කවුද?", "o": ["අලියා", "නිල් තල්මසා", "සිංහයා", "ජිරාෆ්"], "a": "නිල් තල්මසා"},
        {"q": "ජලයේ රසායනික සූත්‍රය කුමක්ද?", "o": ["CO2", "O2", "H2O", "N2"], "a": "H2O"},
        {"q": "පහත ඒවායින් කුමක්ද නිමැවුම් මෙවලමක් (Output Device) වන්නේ?", "o": ["Keyboard", "Mouse", "Monitor", "Scanner"], "a": "Monitor"},
        {"q": "ඉරට ආසන්නතම ග්‍රහලෝකය කුමක්ද?", "o": ["අඟහරු", "බුධ", "සිකුරු", "පෘථිවිය"], "a": "බුධ"},
        {"q": "වර්ණ දේදුන්නක තියෙන වර්ණ ගණන කීයද?", "o": ["5", "6", "7", "8"], "a": "7"},
        {"q": "පෘථිවිය වටා යන ස්වාභාවික චන්ද්‍රයා කවුද?", "o": ["සූර්යයා", "සඳ", "තරු", "
