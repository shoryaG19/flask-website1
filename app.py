from flask import Flask, render_template, request
import os

app = Flask(__name__)

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
    print(f"Message from {name}: {message}")
    return render_template("thanks.html", name=name)

# Bind to 0.0.0.0 and dynamic port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
