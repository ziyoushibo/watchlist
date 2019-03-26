from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/activity')
def activity():
    return render_template('activity.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/xianhua')
def xianhua():
    return render_template('xianhua.html')


@app.route('/guanhai')
def guanhai():
    return render_template('guanhai.html')


@app.route('/hanghai')
def hanghai():
    return render_template('hanghai.html')


@app.route('/chunhuaqiuse')
def chunhuaqiuse():
    return render_template('chunhuaqiuse.html')


@app.route('/binhaisenlin')
def binhaisenlin():
    return render_template('binhaisenlin.html')


@app.route('/shuyuan')
def shuyuan():
    return render_template('shuyuan.html')




