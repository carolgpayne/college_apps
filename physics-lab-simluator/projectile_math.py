# equations: x = v*cos(θ)*t, y = v*sin(θ)*t - 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = 9.81


def user_input():
    while True:
        print("Calculation options\n-------------------")
        print("1. Height")
        print("2. Distance")
        print("3. Range")

        calculation = input("Which would you like to calculate? (1, 2, etc.): ")

        v0 = float(input("Enter initial velocity (m/s): "))
        angle = float(input("Enter initial launch angle (degrees): "))
        time = float(input("Enter the total time: "))

        x_points, y_points, t_points = position(v0, angle, time)

        display_results(calculation, x_points, y_points, v0, angle)

        again = input("Would you like to perform another calculation? (Y/N): ")

        if again.lower() == "n":
            return t_points, x_points, y_points, v0, angle


def position(v0, angle, time):
    # convert degrees to radians, solve for x and y (position)
    radians = np.radians(angle)

    dt = 0.01
    t = 0

    x_points = []
    y_points = []
    t_points = []

    while t <= time:
        x = v0 * np.cos(radians) * t
        y = v0 * np.sin(radians) * t - 0.5 * g * t ** 2

        if y < 0:
            break

        x_points.append(x)
        y_points.append(y)
        t_points.append(t)

        t += dt

    return x_points, y_points, t_points

def display_results(calculation, x_points, y_points, v0, angle):
    if calculation == "1":
        print(f"Final Height: {y_points[-1]:.2f}")
    elif calculation == "2":
            print(f"Final Distance: {x_points[-1]:.2f}")
    elif calculation == "3":
        print(f"Final Position: {x_points[-1]:.2f} , {y_points[-1]:.2f}")
