import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Walentynka?", page_icon="❤️")

# CSS
st.markdown("""
<style>
.stApp {
    background-color: #ffc0cb;
}
header, footer, #MainMenu {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# HTML + JS (bez obrazka!)
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
        body {
            background-color: #ffc0cb;
            font-family: 'Pacifico', cursive;
            margin: 0;
            text-align: center;
        }

        h1 {
            color: #d63384;
            font-size: 2.5rem;
            text-shadow: 2px 2px white;
        }

        button {
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-family: 'Pacifico', cursive;
            margin: 20px;
        }

        #yesBtn {
            background-color: #ff4d6d;
            color: white;
        }

        #noBtn {
            background-color: #f8f9fa;
            color: #6c757d;
            position: absolute;
        }
    </style>
</head>

<body>

<h1>Zostaniesz moją Walentynką? ❤️</h1>
<button id="yesBtn">TAK!</button>
<button id="noBtn">Nie</button>

<script>
    const noBtn = document.getElementById("noBtn");
    const yesBtn = document.getElementById("yesBtn");

    noBtn.addEventListener("mouseover", () => {
        const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
        const y = Math.random() * (window.innerHeight - noBtn.offsetHeight);
        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";
    });

    function fireConfetti() {
        const end = Date.now() + 3000;
        (function frame() {
            confetti({
                particleCount: 6,
                spread: 70,
                origin: { x: Math.random(), y: 0.6 }
            });
            if (Date.now() < end) requestAnimationFrame(frame);
        })();
    }

    yesBtn.addEventListener("click", () => {
        fireConfetti();
        window.parent.postMessage("SHOW_IMAGE", "*");
    });
</script>

</body>
</html>
"""

components.html(html_code, height=300)

# 👇 STREAMLIT CZĘŚĆ — OBRAZEK
if "show" not in st.session_state:
    st.session_state.show = False

# nasłuchiwanie sygnału
st.markdown("""
<script>
window.addEventListener("message", (event) => {
    if (event.data === "SHOW_IMAGE") {
        fetch("/_stcore/message?show=true");
    }
});
</script>
""", unsafe_allow_html=True)

# fallback prosty (klik w checkbox)
show = st.checkbox("")

if show or st.session_state.show:
    st.markdown("## HURRA! Wiedziałem! 😍")
    st.image("hurraa.jpg", use_container_width=True)
