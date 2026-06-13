import matplotlib.pyplot as plt
import numpy as np
import projectile_sim as ps


def user_choice(initial_x, initial_y, v0, angle):
    choice = input(f"1. Graph\n2. Simulate\nWhich would you like?: ")

    if choice == "1":
        graph_position(initial_x, initial_y)
    else:
        simulate_position(initial_x, initial_y, v0, angle)

def graph_position(initial_x, initial_y):
    initial_x = np.linspace(-10, 10, 100)
    initial_y = -initial_x ** 2

    plt.plot(initial_x, initial_y)

    point_x, point_y = initial_x[50], initial_y[50]
    plt.scatter(point_x, point_y, color='red', zorder=5, label=f'Point ({point_x:.2f}, {point_y:.2f})')

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