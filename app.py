from flask import Flask, render_template, request
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# 🏠 Home Page
@app.route('/')
def home():
    return render_template("index.html")

# ℹ️ About Page
@app.route('/about')
def about():
    return render_template("about.html")

# 📞 Contact Page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# ✅ Contact Form Submit → Sends Email
@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    message = request.form['message']

    # 📧 Setup email
    email = EmailMessage()
    email['Subject'] = f"New message from {name}"
    email['From'] = os.environ.get("shoryagupta016@gmail.com")
    email['To'] = os.environ.get("shoryagupta016@gmail.com")
    email.set_content(f"Name: {name}\n\nMessage:\n{message}")

    # 📤 Send email via Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ.get("shoryagupta016@gmail.com"), os.environ.get("nrttpnsqfpbbvhbo"))
            smtp.send_message(email)
        return render_template("thanks.html", name=name)
    except Exception as e:
        return f"❌ Error sending email: {str(e)}"

# 🚀 Run the Flask app (for deployment)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
