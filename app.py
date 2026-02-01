import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="Walentynka?", page_icon="❤️")

# Styl Streamlit
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
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        h1 {
            color: #d63384;
            font-size: 2.5rem;
            text-shadow: 2px 2px white;
            text-align: center;
        }

        .btn-container {
            margin-top: 30px;
            position: relative;
            height: 300px;
            width: 100vw;
            text-align: center;
        }

        button {
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-family: 'Pacifico', cursive;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
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

        #success {
            display: none;
            text-align: center;
        }

        img {
            width: 80%;
            max-width: 500px;
            margin-top: 20px;
            border-radius: 20px;
        }
    </style>
</head>

<body>

<div id="question">
    <h1>Zostaniesz moją Walentynką? ❤️</h1>
    <div class="btn-container">
        <button id="yesBtn">TAK!</button>
        <button id="noBtn">Nie</button>
    </div>
</div>

<div id="success">
    <h1>HURRA! Wiedziałem! 😍</h1>
    <img src="hurraa.jpg" alt="Hurraa Celebration">
</div>

<script>
    const noBtn = document.getElementById("noBtn");
    const yesBtn = document.getElementById("yesBtn");
    const question = document.getElementById("question");
    const success = document.getElementById("success");

    // Uciekające NIE
    noBtn.addEventListener("mouseover", () => {
        const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
        const y = Math.random() * (window.innerHeight - noBtn.offsetHeight);
        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";
    });

    // Konfetti 🎉
    function fireConfetti() {
        const duration = 3000;
        const end = Date.now() + duration;

        (function frame() {
            confetti({
                particleCount: 6,
                spread: 70,
                origin: { x: Math.random(), y: 0.6 }
            });
            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        })();
    }

    // Klik TAK
    yesBtn.addEventListener("click", () => {
        question.style.display = "none";
        success.style.display = "block";
        fireConfetti();
    });
</script>

</body>
</html>
"""

components.html(html_code, height=800)
