import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="Walentynka?", page_icon="❤️")

# CSS dla różowego tła i ukrycia menu Streamlit
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

# Kod HTML, CSS i JS dla efektu "lewitującego" przycisku
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
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
        #container {
            text-align: center;
        }
        h1 {
            color: #d63384;
            font-size: 2.5rem;
            text-shadow: 2px 2px white;
        }
        .btn-container {
            margin-top: 30px;
            position: relative;
            height: 300px;
            width: 100vw;
        }
        button {
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-family: 'Pacifico', cursive;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        #yesBtn {
            background-color: #ff4d6d;
            color: white;
            z-index: 10;
        }
        #noBtn {
            background-color: #f8f9fa;
            color: #6c757d;
            position: absolute;
            transition: all 0.2s ease;
        }
        .gif-container {
            display: none;
            text-align: center;
        }
        img {
            width: 80%;
            max-width: 500px;
            border-radius: 20px;
        }
    </style>
</head>
<body>

    <div id="main-content">
        <h1>Zostaniesz moją Walentynką? ❤️</h1>
        <div class="btn-container">
            <button id="yesBtn">TAK!</button>
            <button id="noBtn">Nie</button>
        </div>
    </div>

    <div id="success-content" class="gif-container">
        <h1>HURRA! Wiedziałem! 😍</h1>
        <img src="https://media1.tenor.com/m/Y-V_87r0Z3AAAAAd/ufc.gif" alt="UFC Celebration">
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainContent = document.getElementById('main-content');
        const successContent = document.getElementById('success-content');

        // Funkcja sprawiająca, że przycisk "Nie" lewituje (porusza się sam)
        let angle = 0;
        function animateNoButton() {
            if (noBtn.style.position !== 'fixed') {
                const x = Math.sin(angle) * 20;
                const y = Math.cos(angle) * 10;
                noBtn.style.transform = `translate(${x}px, ${y}px)`;
                angle += 0.05;
                requestAnimationFrame(animateNoButton);
            }
        }
        animateNoButton();

        // Uciekanie przy próbie najechania myszką
        noBtn.addEventListener('mouseover', function() {
            const x = Math.random() * (window.innerWidth - this.offsetWidth);
            const y = Math.random() * (window.innerHeight - this.offsetHeight);
            
            this.style.position = 'fixed';
            this.style.left = x + 'px';
            this.style.top = y + 'px';
            this.style.transform = 'scale(0.8)'; // Lekko się zmniejsza przy ucieczce
        });

        // Kliknięcie TAK
        yesBtn.addEventListener('click', function() {
            mainContent.style.display = 'none';
            successContent.style.display = 'block';
        });
    </script>
</body>
</html>
"""

# Renderowanie komponentu
components.html(html_code, height=800)
