

from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return

# ngrok command to expose the Flask app
# ngrok command to expose the Flask app
# Replace 5000 with your Flask app's port
# ngrok command to expose the Flask app
# ngrok command to expose the Flask app
# Replace 5000 with your Flask app's port
from pyngrok import ngrok

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
