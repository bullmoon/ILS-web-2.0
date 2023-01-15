from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template('index.html', title='Welcome!')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/table')
def table():
    data = get_data()
    return render_template('table.html', data=data)
