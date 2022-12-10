from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>If you see this page with hellowws.tk. That means you're ready!</p>"