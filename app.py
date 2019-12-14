from flask import Flask, render_template
#from sampling import sample, histogram
from markov import create_sentence


app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html', sentence=create_sentence)
