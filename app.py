from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def generate_password(length, upper, lower, digits, symbols):
    characters = ''
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Select at least one option."

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form["length"])
        upper = "upper" in request.form
        lower = "lower" in request.form
        digits = "digits" in request.form
        symbols = "symbols" in request.form
        password = generate_password(length, upper, lower, digits, symbols)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
