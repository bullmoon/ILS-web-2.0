from flask import Flask, render_template, send_from_directory, request, redirect
import os
from src import tables, datalists

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
    data = tables.get_data()
    br_type = tables.get_breaker()
    return render_template('table.html', data=data, breakers_list=br_type)

@app.route('/brchoice', methods=['GET', 'POST'])
def brchoice():
    breakers = datalists.breakers
    if request.method == 'POST':
        breaker_select = request.form['breaker']
        amperages = breakers[breaker_select]
        return render_template('breakerchoice.html', amperages=amperages)

    return render_template('breakerchoice.html')