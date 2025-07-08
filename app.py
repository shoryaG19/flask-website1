from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
import os, smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash & CSRF protection

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data

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
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f"❌ Error sending message: {str(e)}", "danger")
            return redirect(url_for('contact'))

    return render_template("contact.html", form=form)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
