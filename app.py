import streamlit as st
import random

# ================== KONFIGURACJA ==================
st.set_page_config(page_title="Walentynka?", page_icon="❤️")

# ================== STYL ==================
st.markdown("""
<style>
.stApp {
    background-color: #ffc0cb;
}
header, footer, #MainMenu {
    visibility: hidden;
}
h1, h2 {
    color: #d63384;
    text-shadow: 2px 2px white;
    text-align: center;
}
div.stButton > button {
    font-size: 1.3rem;
    border-radius: 50px;
    padding: 15px 35px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ================== STAN APLIKACJI ==================
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ================== WIDOK STARTOWY ==================
if not st.session_state.accepted:
    st.markdown("## Zostaniesz moją Walentynką? ❤️")

    # losowa pozycja przycisku "Nie"
    left_gap = random.randint(1, 4)
    right_gap = random.randint(1, 4)

    cols = st.columns([left_gap, 2, right_gap])

    # TAK
    with cols[1]:
        if st.button("TAK! 💖"):
            st.session_state.accepted = True
            st.balloons()  # 🎉 konfetti

    # NIE (ucieka)
    if random.choice([True, False]):
        with cols[0]:
            st.button("Nie 😅")
    else:
        with cols[2]:
            st.button("Nie 🙈")

# ================== WIDOK PO KLIKNIĘCIU TAK ==================
else:
    st.markdown("## HURRA! Wiedziałem! 😍")
    st.image("hurraa.jpg", use_container_width=True)
