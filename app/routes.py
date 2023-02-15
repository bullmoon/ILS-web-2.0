from flask import Flask, render_template, send_from_directory, request, redirect
import os
from flask_mysqldb import MySQL
from src import tables, datalists
import config

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object('config')

# Create an instance of the MySQL class
mysql = MySQL(app)

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

# Use the connection in a view function
@app.route('/testsql')
def testsql():
    cur = mysql.connection.cursor()
    cur.execute('SELECT breaker FROM breakers')
    data = cur.fetchall()
    return str(data)