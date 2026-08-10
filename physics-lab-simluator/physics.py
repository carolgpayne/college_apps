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

    data = request.get_json()

    velocity = float(data["velocity"])
    angle = float(data["angle"])
    time = float(data["time"])

    projectile = Projectile(velocity, angle)
    projectile.position(time)

    #gp.graph_position(projectile)
    #gp.simulate_position(projectile)

    filename = "trajectory.csv"
    ci.save_data(filename, projectile)

    analysis = Analysis(data)

    return jsonify({

    })

if __name__ == "__main__":
    app.run(debug=True)
