from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze", methods=["post"])
def analyze():
    input_text = request.form["input_text"]
    word_count = len(input_text.split())
    return render_template("analyze.html",text=input_text, word_count = word_count)

@app.route("/banana")
def banana():
    return "Banana"

from loader import load_AFINN, load_rhetoric_words

lexicon = load_AFINN()
rhetoric_words = load_rhetoric_words()
