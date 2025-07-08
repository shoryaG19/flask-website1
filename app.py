from flask import Flask, render_template, request, flash, redirect, url_for
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super_secret_key_123")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    message = request.form['message']

    email = EmailMessage()
    email['Subject'] = f"New message from {name}"
    email['From'] = os.environ.get("EMAIL_USER")
    email['To'] = os.environ.get("EMAIL_RECEIVER")
    email.set_content(f"Name: {name}\n\nMessage:\n{message}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
            smtp.send_message(email)
        flash("✅ Message sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Failed to send message: {str(e)}", "error")

    return redirect(url_for('contact'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
