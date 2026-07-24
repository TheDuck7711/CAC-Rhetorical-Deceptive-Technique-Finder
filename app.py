from flask import Flask, render_template, request
from analyzers import rhetoric_spotter, sentiment_analysis

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze", methods=["post"])
def analyze():
    input_text = request.form["input_text"]
    sentiment_analysis_results = sentiment_analysis(input_text)
    rhetoric_spotter_results = rhetoric_spotter(input_text)
    word_count = len(input_text.split())
    return render_template("analyze.html",text=input_text, word_count = word_count, abs_avg = sentiment_analysis_results[0],
                            net_avg = sentiment_analysis_results[1], range_high = sentiment_analysis_results[2],
                            range_low = sentiment_analysis_results[3], numb_rhetoric = rhetoric_spotter_results[0], percent_rhetoric = rhetoric_spotter_results[1],
                            list_rhetoric = rhetoric_spotter_results[2])

@app.route("/banana")
def banana():
    return "Banana"

from loader import load_AFINN, load_rhetoric_words

lexicon = load_AFINN()
rhetoric_words = load_rhetoric_words()
