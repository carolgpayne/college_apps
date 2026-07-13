import matplotlib.pyplot as plt
import numpy as np
from visualization import projectile_sim as ps
from Inputs import projectile_math as pm
from Inputs.projectile_math import Projectile

def user_choice(projectile):
    choice = input(f"1. Graph\n2. Simulate\nWhich would you like?: ")

    if choice == "1":
        graph_position(projectile.x_points, projectile.y_points)
    else:
        simulate_position(projectile.v0, projectile.angle)

def graph_position(x_points, y_points):
    plt.plot(x_points, y_points, label="Theoretical Trajectory")

    plt.title("Predicted Projectile Path")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

def simulate_position(v0, angle):
    x_points, y_points, t_points = ps.simulate_projectile(v0, angle)

    plt.plot(x_points, y_points, label="Simulation")

    plt.title("Simulated Projectile Path")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()