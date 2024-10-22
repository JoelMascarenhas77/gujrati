from flask import Flask, render_template, request
from prepro import tokenize_and_filter
from compute import calculate_similarity
import pickle


app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    similarity_scores = None
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        text1 = tokenize_and_filter(text1)
        text2 = tokenize_and_filter(text2)

        similarity_scores= calculate_similarity(text1, text2)

    return render_template('index.html', similarity_scores=similarity_scores)

if __name__ == '__main__':
    app.run(debug=True)
