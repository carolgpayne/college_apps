# equations: x = v*cos(θ)*t, y = v*sin(θ)*t + 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = 9.81

def choices():
    print("Calculation options" + "\n" + "-------------------")
    print("1. Height")
    print("2. Distance")
    print("3. Range")

    calculation = input("Which would you like to calculate? (1, 2, etc.): ")

    return position(calculation)

def position(calculation):
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    launch_angle = float(input("Enter initial launch angle (degrees): "))
    total_time = float(input("Enter the total time: "))
    # convert degrees to radians, solve for x and y (position)
    radians = np.radians(launch_angle)

    # time array for graphing
    t_vals = np.linspace(0, total_time, 50)

    x_vals = initial_velocity * np.cos(radians) * t_vals
    y_vals = initial_velocity * np.sin(radians) * t_vals + 0.5 * g * t_vals ** 2

    if calculation == "1":
        print("Final Height: ", y_vals[-1])
        new_calc = input("Would you like to perform another calculation? (Y/N): ")
        if new_calc == "Y" or new_calc == "y":
            choices()
    elif calculation == "2":
        print("Final Distance: ", x_vals[-1])
        new_calc = input("Would you like to perform another calculation? (Y/N): ")
        if new_calc == "Y" or new_calc == "y":
            choices()
    elif calculation == "3":
        print("Final Position: ", x_vals[-1], y_vals[-1])

    return x_vals, y_vals, initial_velocity, launch_angle, total_time