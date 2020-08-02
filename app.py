from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    a = "Welcome to Menu Bitch"
    return a