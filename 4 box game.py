import streamlit as st
import random

# පිටුවේ සැකසුම් සහ Theme එක
st.set_page_config(page_title="Magic Box Quiz", layout="centered")

# --- Custom CSS (ලස්සන කරන්න) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 100px;
        border-radius: 15px;
        font-size: 20px;
        font-weight: bold;
        background-color: #FF4B4B;
        color: white;
        transition: 0.3s;
        border: 2px solid #f0f2f6;
    }
    .stButton>button:hover {
        background-color: #FF8080;
        transform: scale(1.05);
        border: 2px solid #FF4B4B;
    }
    .main {
        background-color: #f0f2f6;
    }
    .score-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State කළමනාකරණය
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.status = "selecting_box" # selecting_box, show_question, box_missed

# ප්‍රශ්න 20ක් (මම උදාහරණ 5ක් දාන්නම්, ඔබට තව එකතු කළ හැක)
questions = [
    {"q": "පරිගණකයේ දත්ත තාවකාලිකව ගබඩා කරන්නේ කොහේද?", "options": ["Hard Disk", "RAM", "CPU", "Mouse"], "a": "RAM"},
    {"q": "සූර්යග්‍රහ මණ්ඩලයේ විශාලම ග්‍රහලෝකය කුමක්ද?", "options": ["අඟහරු", "සෙනසුරු", "බ්‍රහස්පති", "පෘථිවිය"], "a": "බ්‍රහස්පති"},
    {"q": "ලොව වේගවත්ම සතා කවුද?", "options": ["සිංහයා", "කොටියා", "චීටා", "අලියා"], "a": "චීටා"},
    {"q": "ජලයේ රසායනික සංකේතය කුමක්ද?", "options": ["CO2", "H2O", "O2", "NaCl"], "a": "H2O"},
    {"q": "ශ්‍රී ලංකාවේ උසම කන්ද කුමක්ද?", "options": ["නමුනුකුල", "සමනල කන්ද", "පිදුරුතලාගල", "බිබිලේ කන්ද"], "a": "පිදුරුතලාගල"},
]

def reset_game():
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.status = "selecting_box"
    st.rerun()

# --- Game Logic ---
if not st.session_state.game_over:
    curr = st.session_state.q_idx
    total = len(questions)

    st.title("✨ Magic Box Education Game")
    
    # ලකුණු සහ ප්‍රගතිය පෙන්වන පුවරුව
    cols_top = st.columns(2)
    cols_top[0].metric("ප්‍රශ්නය", f"{curr + 1} / {total}")
    cols_top[1].metric("ලකුණු", st.session_state.score)

    st.divider()

    # 1. කොටු තේරීමේ අවස්ථාව
    if st.session_state.status == "selecting_box":
        st.subheader("ප්‍රශ්නය සැඟවී ඇති කොටුව තෝරන්න! 🎁")
        
        # Target box එක තීරණය කිරීම
        if 'target' not in st.session_state or st.session_state.last_q != curr:
            st.session_state.target = random.randint(1, 4)
            st.session_state.last_q = curr

        boxes = st.columns(4)
        for i in range(4):
            if boxes[i].button(f"📦\nBox {i+1}", key=f"b{curr}_{i}"):
                if (i + 1) == st.session_state.target:
                    st.session_state.status = "show_question"
                else:
                    st.session_state.status = "box_missed"
                st.rerun()

    # 2. වැරදි කොටුවක් තේරූ විට
    elif st.session_state.status == "box_missed":
        st.error("අපොයි! ඔබ තේරූ කොටුවේ ප්‍රශ්නය නැහැ. ❌")
        st.info(f"නිවැරදි කොටුව වුණේ: Box {st.session_state.target}")
        if st.button("ඊළඟ ප්‍රශ්නයට යන්න ➡️"):
            if st.session_state.q_idx < total - 1:
                st.session_state.q_idx += 1
                st.session_state.status = "selecting_box"
            else:
                st.session_state.game_over = True
            st.rerun()

    # 3. හරි කොටුව තේරූ විට (ප්‍රශ්නය පෙන්වීම)
    elif st.session_state.status == "show_question":
        st.success("නියමයි! ප්‍රශ්නය හමු වුණා. 🎉")
        st.markdown(f"### {questions[curr]['q']}")
        
        ans = st.radio("නිවැරදි පිළිතුර තෝරන්න:", questions[curr]['options'], index=None)
        
        if st.button("පිළිතුර තහවුරු කරන්න ✅"):
            if ans == questions[curr]['a']:
                st.session_state.score += 1
                st.toast("නිවැරදියි! +1", icon="✅")
            else:
                st.toast("වැරදියි!", icon="❌")
            
            if st.session_state.q_idx < total - 1:
                st.session_state.q_idx += 1
                st.session_state.status = "selecting_box"
            else:
                st.session_state.game_over = True
            st.rerun()

# --- Game Over Screen ---
else:
    st.balloons()
    st.markdown("<div class='score-box'>", unsafe_allow_html=True)
    st.title("🏆 තරගය අවසන්!")
    st.header(f"ඔබේ අවසන් ලකුණු සංඛ්‍යාව: {st.session_state.score} / {len(questions)}")
    
    performance = (st.session_state.score / len(questions)) * 100
    if performance >= 80:
        st.success("ඉතා විශිෂ්ටයි! 🌟")
    elif performance >= 50:
        st.warning("හොඳයි, තව උත්සාහ කරන්න! 👍")
    else:
        st.error("නැවත උත්සාහ කර දැනුම වැඩි කරගන්න! 📚")
        
    if st.button("නැවත ක්‍රීඩා කරන්න 🔄"):
        reset_game()
    st.markdown("</div>", unsafe_allow_html=True)
