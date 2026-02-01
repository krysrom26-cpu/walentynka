import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="Walentynkowe Pytanie", page_icon="❤️", layout="centered")

# Stylizacja tła aplikacji na różowo za pomocą CSS
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

# Cała logika aplikacji (pytanie, uciekający przycisk i GIF) w jednym komponencie HTML/JS
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #ffc0cb;
            font-family: 'Pacifico', cursive;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        #container {
            text-align: center;
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        h1 {
            color: #d63384;
            font-size: 3rem;
            margin-bottom: 50px;
            text-shadow: 2px 2px white;
        }
        .buttons {
            position: relative;
            width: 100%;
            height: 200px;
        }
        button {
            padding: 15px 30px;
            font-size: 1.5rem;
            border-radius: 15px;
            border: none;
            cursor: pointer;
            font-family: 'Pacifico', cursive;
            transition: transform 0.2s;
        }
        #yesBtn {
            background-color: #ff4d6d;
            color: white;
            position: absolute;
            left: 50%;
            transform: translateX(-120%);
        }
        #noBtn {
            background-color: #6c757d;
            color: white;
            position: absolute;
            left: 50%;
            transform: translateX(20%);
        }
        #success-screen {
            display: none;
        }
        .jump-gif {
            width: 300px;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>

    <div id="container">
        <div id="proposal-screen">
            <h1>Zostaniesz moją Walentynką? ❤️</h1>
            <div class="buttons">
                <button id="yesBtn">TAK!</button>
                <button id="noBtn">Nie</button>
            </div>
        </div>

        <div id="success-screen">
            <h1>HURRA! Wiedziałem! 😍</h1>
            <img class="jump-gif" src="https://media.giphy.com/media/lMameLqvJo9UCW8d6Z/giphy.gif" alt="Cieszący się facet">
        </div>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const proposalScreen = document.getElementById('proposal-screen');
        const successScreen = document.getElementById('success-screen');

        // Funkcja uciekania przycisku "Nie"
        noBtn.addEventListener('mouseover', function() {
            const x = Math.random() * (window.innerWidth - this.offsetWidth);
            const y = Math.random() * (window.innerHeight - this.offsetHeight);
            
            this.style.position = 'fixed';
            this.style.left = x + 'px';
            this.style.top = y + 'px';
            this.style.transform = 'none'; // usuwamy centrowanie przy ruchu
        });

        // Obsługa kliknięcia "TAK"
        yesBtn.addEventListener('click', function() {
            proposalScreen.style.display = 'none';
            successScreen.style.display = 'block';
        });
    </script>
</body>
</html>
"""

# Wyświetlenie komponentu na całą szerokość
components.html(html_code, height=600)
