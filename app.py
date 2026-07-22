from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CAC Rhetoric blah blah blah"

@app.route("/banana")
def banana():
    return "Banana"

from analyzer import load_AFINN, load_rhetoric_words

lexicon = load_AFINN()
rhetoric_words = load_rhetoric_words()
