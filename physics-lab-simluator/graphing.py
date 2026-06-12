import matplotlib.pyplot as plt
import numpy as np
import projectile_sim as ps


def user_choice(initial_x, initial_y, v0, angle):
    choice = input("1. Graph" + "\n" + "2. Simulate" + "\n" + "Which would you like?: ")

    if choice == "1":
        graph_position()
    else:
        simulate_position(initial_x, initial_y, v0, angle)

def graph_position():
    x = np.linspace(-10, 10, 100)
    y = -x ** 2

    plt.plot(x, y)

    point_x, point_y = x[50], y[50]
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