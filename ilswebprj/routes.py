from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template('index.html', title='Welcome!')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/table')
def index():
    data = get_data()
    return render_template('table.html', data=data)
