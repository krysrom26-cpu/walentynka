import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Walentynkowe Pytanie", page_icon="❤️")

# Stylowanie tła na różowo i ukrycie standardowych elementów Streamlit
st.markdown("""
    <style>
    .stApp {
        background-color: #ffc0cb;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

if 'clicked_yes' not in st.session_state:
    st.session_state.clicked_yes = False

if not st.session_state.clicked_yes:
    st.markdown("<h1 style='text-align: center; color: #d63384;'>Zostaniesz moją Walentynką? ❤️</h1>", unsafe_allow_html=True)
    
    # Interaktywne przyciski w HTML/JS
    html_code = """
    <div id="container" style="height: 300px; position: relative; text-align: center; padding-top: 50px;">
        <button id="yesBtn" style="font-size: 20px; padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; margin-right: 50px;">TAK!</button>
        <button id="noBtn" style="font-size: 20px; padding: 10px 20px; background-color: #dc3545; color: white; border: none; border-radius: 5px; position: absolute;">Nie</button>
    </div>

    <script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');

    noBtn.addEventListener('mouseover', () => {
        const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
        const y = Math.random() * (300 - noBtn.offsetHeight);
        noBtn.style.left = x + 'px';
        noBtn.style.top = y + 'px';
    });

    yesBtn.addEventListener('click', () => {
        window.parent.postMessage({type: 'streamlit:set_component_value', value: true}, '*');
    });
    </script>
    """
    
    # Przechwycenie kliknięcia w "TAK" przez komponent Streamlit
    result = components.html(html_code, height=400)
    if result:
        st.session_state.clicked_yes = True
        st.rerun()

else:
    st.markdown("<h1 style='text-align: center; color: #d63384;'>HURRA! Wiedziałem! 😍</h1>", unsafe_allow_html=True)
    # Link do gifa z cieszącym się facetem
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZ3bmZ3bmZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/lMameLqvJo9UCW8d6Z/giphy.gif", use_container_width=True)
    
    if st.button("Zacznij od nowa"):
        st.session_state.clicked_yes = False
        st.rerun()
