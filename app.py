from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CAC Rhetoric blah blah blah"

@app.route("/banana")
def banana():
    return "Banana"