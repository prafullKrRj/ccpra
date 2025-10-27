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
    <title>Our Team Project</title>
    <style>
        /* Define the new color palette */
        :root {
            --color-primary: #00b4d8; /* Bright Cyan/Blue */
            --color-secondary: #0077b6; /* Darker Blue/Indigo */
            --color-text-light: #666;
            --color-text-dark: #333;
            --color-background-light: rgba(255, 255, 255, 0.95);
            --color-section-bg: #f8f9fa;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            /* Updated Gradient */
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-secondary) 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: var(--color-background-light);
            border-radius: 20px;
            padding: 50px;
            max-width: 900px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            animation: fadeIn 1s ease-in;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h1 {
            font-size: 2.5rem;
            color: var(--color-primary); /* Updated Color */
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }

        .subtitle {
            text-align: center;
            color: var(--color-text-light);
            font-size: 1.2rem;
            margin-bottom: 40px;
        }

        .team-section {
            margin-top: 30px;
        }

        .team-title {
            font-size: 1.8rem;
            color: var(--color-secondary); /* Updated Color */
            text-align: center;
            margin-bottom: 30px;
            font-weight: 600;
        }

        .team-grid {
            /* Modified to better center a single card */
            display: flex; 
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .team-member {
            /* Updated Gradient */
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-secondary) 100%);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            color: white;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            /* Ensure single card has a max width */
            max-width: 300px; 
            width: 100%;
        }

        .team-member:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }

        .member-icon {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        .member-name {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .member-role {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .info-section {
            background: var(--color-section-bg);
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
        }

        .info-title {
            font-size: 1.5rem;
            color: var(--color-primary); /* Updated Color */
            margin-bottom: 15px;
            font-weight: 600;
        }

        .info-text {
            color: var(--color-text-light);
            line-height: 1.8;
            font-size: 1.1rem;
        }

        .highlight {
            color: var(--color-secondary); /* Updated Color */
            font-weight: 600;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            color: #888;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 30px 20px;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            /* Ensure it stays centered on mobile */
            .team-grid {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Welcome to Our Project</h1>
        <p class="subtitle">A Flask-based Web Application for Cloud Computing</p>
        
        <div class="team-section">
            <h2 class="team-title">👥 Our Team Member</h2>
            
            <div class="team-grid">
                <!-- Single Team Member Card -->
                <div class="team-member">
                    <div class="member-icon">👤</div>
                    <div class="member-name">Abhishek Kumar</div>
                    <div class="member-role">Lead Developer</div>
                </div>
            </div>
        </div>
        
        <div class="info-section">
            <h3 class="info-title">📝 About This Project</h3>
            <p class="info-text">
                This is a <span class="highlight">Flask web application</span> created by our team. 
                Flask is a lightweight and powerful web framework for Python that allows us to build 
                beautiful and functional web applications. This project demonstrates our understanding 
                of <span class="highlight">web development</span>, <span class="highlight">HTML</span>, 
                <span class="highlight">CSS</span>, and <span class="highlight">Python</span>.
            </p>
        </div>
        
        <div class="footer">
            <p>🚀 Powered by Flask | Made with ❤️ by our team</p>
        </div>
    </div>
</body>
</html>

"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
