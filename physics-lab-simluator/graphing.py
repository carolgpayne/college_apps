import matplotlib.pyplot as plt
import numpy as np
import projectile_sim as ps


def user_choice(x_points, y_points, v0, angle):
    choice = input(f"1. Graph\n2. Simulate\nWhich would you like?: ")

    if choice == "1":
        graph_position(x_points, y_points)
    else:
        simulate_position(x_points, y_points, v0, angle)

def graph_position(x_points, y_points):

    plt.plot(x_points, y_points)

    plt.title("Predicted Projectile Path")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

def simulate_position(initial_x, initial_y, v0, angle):
    x, y, t = ps.simulate_projectile(initial_x, initial_y, v0, angle)

    plt.plot(x, y)
    plt.show()