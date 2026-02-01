import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="Walentynka?", page_icon="❤️")

# Zakodowany gif w formacie Base64 (pełny kod)
gif_data = "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"

# CSS dla głównej aplikacji Streamlit
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

# Kod HTML, CSS i JS z poprawkami wyświetlania
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: #ffc0cb;
            font-family: 'Pacifico', cursive;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: flex-start; /* Zmienione na start, aby zapobiec ucinaniu góry */
            min-height: 100vh;
            text-align: center;
        }}
        .content-wrapper {{
            width: 100%;
            max-width: 600px;
            margin-top: 50px;
        }}
        h1 {{
            color: #d63384;
            font-size: 2.2rem;
            text-shadow: 2px 2px white;
            margin-bottom: 20px;
        }}
        .btn-container {{
            position: relative;
            height: 300px;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        button {{
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-family: 'Pacifico', cursive;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        #yesBtn {{
            background-color: #ff4d6d;
            color: white;
            z-index: 10;
        }}
        #noBtn {{
            background-color: #f8f9fa;
            color: #6c757d;
            position: absolute;
            transition: all 0.2s ease;
        }}
        .gif-container {{
            display: none;
            width: 100%;
        }}
        img {{
            width: 100%;
            max-width: 450px;
            height: auto;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>

    <div class="content-wrapper">
        <div id="main-content">
            <h1>Zostaniesz moją Walentynką? ❤️</h1>
            <div class="btn-container">
                <button id="yesBtn">TAK!</button>
                <button id="noBtn">Nie</button>
            </div>
        </div>

        <div id="success-content" class="gif-container">
            <h1>HURRA! Wiedziałem! 😍</h1>
            <img src="data:image/gif;base64,{gif_data}" alt="UFC Celebration">
        </div>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainContent = document.getElementById('main-content');
        const successContent = document.getElementById('success-content');

        let angle = 0;
        function animateNoButton() {{
            if (noBtn.style.position !== 'fixed') {{
                const x = Math.sin(angle) * 20;
                const y = Math.cos(angle) * 10;
                noBtn.style.transform = `translate(${{x}}px, ${{y}}px)`;
                angle += 0.05;
                requestAnimationFrame(animateNoButton);
            }}
        }}
        animateNoButton();

        noBtn.addEventListener('mouseover', function() {{
            const x = Math.random() * (window.innerWidth - this.offsetWidth);
            const y = Math.random() * (window.innerHeight - this.offsetHeight);
            
            this.style.position = 'fixed';
            this.style.left = x + 'px';
            this.style.top = y + 'px';
            this.style.transform = 'scale(0.8)';
        }});

        yesBtn.addEventListener('click', function() {{
            mainContent.style.display = 'none';
            successContent.style.display = 'block';
        }});
    </script>
</body>
</html>
"""

# Renderowanie komponentu z dużą wysokością i włączonym przewijaniem
components.html(html_code, height=1000, scrolling=True)
