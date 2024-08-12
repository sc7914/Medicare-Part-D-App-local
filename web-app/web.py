!pip install flask-ngrok
from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return

!ngrok http 5000  # Replace 5000 with your Flask app's port

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

app.run()

if __name__ == '__main__':
    app.run(debug=True)
