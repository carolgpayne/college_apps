from flask import Flask, render_template, request, jsonify
from Inputs.projectile_math import Projectile
from visualization import graphing as gp
from analysis import csv_io as ci
from analysis.data_analysis import Analysis

app = Flask(__name__)

@app.route("/")
def physics_lab():
    return render_template("main_interface.html")

@app.route("/physics")
def physics():
    return render_template("physics_interface.html")

@app.route("/simulate", methods=["POST"])
def simulate():

    value = request.get_json()

    velocity = float(value["velocity"])
    angle = float(value["angle"])
    time = float(value["time"])

    projectile = Projectile(velocity, angle)
    projectile.position(time)

    filename = "trajectory.csv"
    ci.save_data(filename, projectile)
    data = ci.load_data(filename)

    analysis = Analysis(data)

    return jsonify({
        "max_height": analysis.max_height,
        "total_distance": analysis.total_distance
    })

if __name__ == "__main__":
    app.run(debug=True)
