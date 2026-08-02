from flask import Flask, render_template, request
from analyzers import sentiment_analysis,rhetoric_spotter_v2,repitition_spotter,word_cleaner

app = Flask(__name__)

from loader import load_AFINN, load_rhetoric_words

lexicon = load_AFINN()
rhetoric_words = load_rhetoric_words()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze_v2", methods=["post"])
def analyze_v2():
    input_text = request.form["input_text"]
    exclude_quotes = request.form["exclude_quotes"]
    sentiment_analysis_results = sentiment_analysis(word_cleaner(input_text, exclude_quotes))
    rhetoric_spotter_results = rhetoric_spotter_v2(word_cleaner(input_text, exclude_quotes))
    repitition_spotter_results = repitition_spotter(word_cleaner(input_text, exclude_quotes))
    word_count = len(input_text.split())
    return render_template("analyze_v2.html",text=input_text, word_count = word_count, abs_avg = sentiment_analysis_results[0],
                            net_avg = sentiment_analysis_results[1], range_high = sentiment_analysis_results[2],
                            range_low = sentiment_analysis_results[3], numb_rhetoric = rhetoric_spotter_results[0], percent_rhetoric = rhetoric_spotter_results[1],
                            dict_rhetoric = rhetoric_spotter_results[2], numb_repeated_words = repitition_spotter_results[0], 
                            dict_repeated_words = repitition_spotter_results[1])

@app.route("/banana")
def banana():
    return "Banana"

