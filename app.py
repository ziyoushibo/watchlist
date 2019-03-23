from flask import Flask,url_for
app = Flask(__name__)

@app.route('/apple')
@app.route('/hhww')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/test') 
def test():
    print(url_for('hello'))
    return url_for('hello')
