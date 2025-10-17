# from flask import Flask
# # If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# # called `app` in `main.py`.
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     """Return a friendly HTTP greeting.
#     Returns:
#         A string with the words 'Hello World!'.
#     """
#     return "Hello World!"
# if __name__ == "__main__":
#     # This is used when running locally only. When deploying to Google App
#     # Engine, a webserver process such as Gunicorn will serve the app. You
#     # can configure startup instructions by adding `entrypoint` to app.yaml.
#     app.run(host="127.0.0.1", port=8080, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a crazy, animated webpage with stunning visuals."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 CRAZY PAGE 🌈</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            overflow-x: hidden;
            background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff00ff);
            background-size: 400% 400%;
            animation: gradientShift 8s ease infinite;
            min-height: 100vh;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }

        h1 {
            font-size: 5rem;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(45deg, #fff, #ff0080, #00ffff, #fff);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGlow 3s ease infinite, bounce 2s ease-in-out infinite;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
            margin-bottom: 30px;
        }

        @keyframes textGlow {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            25% { transform: translateY(-20px) rotate(-5deg); }
            75% { transform: translateY(-10px) rotate(5deg); }
        }

        .emoji-container {
            display: flex;
            gap: 20px;
            font-size: 4rem;
            margin-bottom: 40px;
        }

        .emoji {
            animation: spin 3s linear infinite, rainbow 2s ease-in-out infinite;
            cursor: pointer;
            transition: transform 0.3s;
        }

        .emoji:hover {
            transform: scale(1.5) rotate(360deg);
        }

        .emoji:nth-child(1) { animation-delay: 0s; }
        .emoji:nth-child(2) { animation-delay: 0.3s; }
        .emoji:nth-child(3) { animation-delay: 0.6s; }
        .emoji:nth-child(4) { animation-delay: 0.9s; }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes rainbow {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(360deg); }
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 2px solid rgba(255, 255, 255, 0.2);
            animation: float 4s ease-in-out infinite;
            max-width: 600px;
            text-align: center;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(2deg); }
        }

        .card p {
            color: white;
            font-size: 1.5rem;
            line-height: 1.8;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        }

        .button {
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            border: none;
            color: white;
            padding: 15px 40px;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            animation: pulse 2s ease-in-out infinite;
            transition: all 0.3s;
        }

        .button:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        @keyframes pulse {
            0%, 100% { box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
            50% { box-shadow: 0 5px 30px rgba(255,0,255,0.8); }
        }

        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s ease-in-out infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
        }

        .circle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            animation: expand 5s ease-out infinite;
        }

        @keyframes expand {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            100% {
                transform: scale(2);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    
    <div class="container">
        <h1>🌟 SUNDAR'S CRAZY PAGE 🌟</h1>
        
        <div class="emoji-container">
            <span class="emoji">🚀</span>
            <span class="emoji">🌈</span>
            <span class="emoji">⚡</span>
            <span class="emoji">🎨</span>
        </div>
        
        <div class="card">
            <p>✨ Welcome to the most INSANE webpage ever! ✨</p>
            <p>🎭 Where chaos meets creativity! 🎭</p>
            <p>💫 Powered by Flask & Pure Awesomeness 💫</p>
            <button class="button" onclick="explode()">CLICK ME! 💥</button>
        </div>
    </div>

    <script>
        // Create random stars
        const starsContainer = document.getElementById('stars');
        for (let i = 0; i < 50; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.width = Math.random() * 3 + 'px';
            star.style.height = star.style.width;
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 3 + 's';
            starsContainer.appendChild(star);
        }

        // Explosive button effect
        function explode() {
            const colors = ['#ff00ff', '#00ffff', '#ffff00', '#ff0080', '#00ff00'];
            for (let i = 0; i < 20; i++) {
                const circle = document.createElement('div');
                circle.className = 'circle';
                circle.style.width = Math.random() * 100 + 50 + 'px';
                circle.style.height = circle.style.width;
                circle.style.left = Math.random() * 100 + '%';
                circle.style.top = Math.random() * 100 + '%';
                circle.style.background = colors[Math.floor(Math.random() * colors.length)];
                circle.style.animationDelay = Math.random() * 0.5 + 's';
                document.body.appendChild(circle);
                
                setTimeout(() => circle.remove(), 5000);
            }
            
            alert('🎉 BOOM! You unleashed the CRAZY! 🎉');
        }

        // Make emojis interactive
        document.querySelectorAll('.emoji').forEach(emoji => {
            emoji.addEventListener('click', function() {
                this.style.animation = 'none';
                setTimeout(() => {
                    this.style.animation = '';
                }, 10);
            });
        });
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
