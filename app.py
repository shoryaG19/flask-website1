from flask import Flask, render_template, request, flash, redirect, url_for
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

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

# 💼 Projects Page
@app.route('/projects')
def projects():
    return render_template("projects.html")

# ✅ Contact Form Submission Handler
@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    message = request.form['message']

    email = EmailMessage()
    email['Subject'] = f"New message from {name}"
    email['From'] = os.environ.get("EMAIL_USER")  # Example: your Gmail
    email['To'] = os.environ.get("EMAIL_RECEIVER")  # Receiver email (can be same)

    email.set_content(f"Name: {name}\n\nMessage:\n{message}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
            smtp.send_message(email)
        flash("✅ Message sent successfully!", "success")
        return redirect(url_for('contact'))
    except Exception as e:
        flash(f"❌ Error sending message: {str(e)}", "danger")
        return redirect(url_for('contact'))

# 🚀 Flask App Runner
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render default port
    app.run(host='0.0.0.0', port=port)
