from flask import Flask

app = Flask(__name__)

@app.route("/")
def physics_lab():
    return "<h1>Physics Lab Simulator</h1>"
