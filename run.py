from flask import Flask

app = Flask(__name__)

# your application routes and views

if __name__ == '__main__':
    app.run(debug=True)
