!pip install flask
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import requests
import json
import os


app = Flask(__name__)

run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return "<p>Hello, World!</p>"

app.run()

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return

# ngrok command to expose the Flask app
ngrok.connect(5000)
# Replace 5000 with your Flask app's port
from pyngrok import ngrok
from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

app.run()

if __name__ == '__main__':
    app.run(debug=True)

# Run ngrok to expose the Flask app
ngrok.connect(5000)


app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

app.run()

if __name__ == '__main__':
    app.run(debug=True)
