from Calculations import projectile_math as pm
import numpy as np

def time(x_vals, y_vals, initial_velocity, launch_angle, total_time):
    initial_position = x_vals, y_vals
    g = 9.81 # downward, negative

    rad = np.radians(launch_angle)
    v_x = initial_velocity * np.cos(rad)
    v_y = initial_velocity * np.sin(rad) + g*total_time

    print(v_x, v_y)