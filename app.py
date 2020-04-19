from flask import Flask
from flask import render_template, redirect, request
import model

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/')
@app.route('/home')
def home():
    dataset = model.get_player_info()
    return render_template('home.html', dataset=dataset[0:20])


@app.route('/player')
def player():
    return render_template('player.html')


@app.route('/player/<full_name>', methods=['GET'])
def player_name(full_name):
    return render_template('player.html', full_name=full_name)


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/sparqlSearch')
def sparql_search():
    return render_template('sparqlSearch.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)