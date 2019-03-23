from flask import Flask, url_for, render_template
app = Flask(__name__)

name = 'guoshibo'
movies = [
    {'title': 'my neighbor totoro', 'year': '1988'},
    {'title': 'dead poets society', 'year': '1989'},
    {'title': 'a perfect world', 'year': '1993'},
    {'title': 'leon', 'year': '1994'},
    {'title': 'mahjong', 'year': '1996'},
    {'title': 'swallottail butterfly', 'year': '1999'},
    {'title': 'king if comedy', 'year': '1999'},
    {'title': 'devils on the doorstep', 'year': '1999'},
    {'title': 'wall-e', 'year': '2008'},
    {'title': 'the pork if music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name= name, movies= movies)



