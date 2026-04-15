import matplotlib.pyplot as plt
import numpy as np

def graph_position():
    x_vals = np.linspace(-10, 10, 100)
    y_vals = -x_vals**2

    plt.plot(x_vals, y_vals)

    point_x, point_y = x_vals[50], y_vals[50]
    plt.scatter(point_x, point_y, color='red', zorder=5, label=f'Point ({point_x:.2f}, {point_y:.2f})')

    plt.title("Predicted Projectile Path")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()
