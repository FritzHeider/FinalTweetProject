from flask import Flask, render_template
from sampling import sample, histogram
# from markov import generate_sentence

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', sentence="Hello")
