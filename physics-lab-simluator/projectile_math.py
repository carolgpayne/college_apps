# equations: x = v*cos(θ)*t, y = v*sin(θ)*t - 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = 9.81


def user_input():
    while True:
        print("Calculation options" + "\n" + "-------------------")
        print("1. Height")
        print("2. Distance")
        print("3. Range")

        calculation = input("Which would you like to calculate? (1, 2, etc.): ")

        v0 = float(input("Enter initial velocity (m/s): "))
        angle = float(input("Enter initial launch angle (degrees): "))
        time = float(input("Enter the total time: "))

        x_points, y_points = position(calculation, v0, angle, time)

        display_results(calculation, x_points, y_points, v0, angle)

        again = input("Would you like to perform another calculation? (Y/N): ")

        if again.lower() == "n":
            return x_points, y_points, v0, angle


def position(calculation, v0, angle, time):
    # convert degrees to radians, solve for x and y (position)
    radians = np.radians(angle)

    t_vals = np.linspace(0, time, 50)

    x_points = v0 * np.cos(radians) * t_vals
    y_points = v0 * np.sin(radians) * t_vals - 0.5 * g * t_vals ** 2

    return x_points, y_points

def display_results(calculation, x_points, y_points, v0, angle):
    if calculation == "1":
        print("Final Height: ", y_points[-1])
    elif calculation == "2":
            print("Final Distance: ", x_points[-1])
    elif calculation == "3":
        print("Final Position: ", x_points[-1], y_points[-1])
