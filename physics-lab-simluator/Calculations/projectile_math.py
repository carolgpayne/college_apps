# equations: x = v*cos(θ)*t, y = v*sin(θ)*t - 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = -9.81

def choices():
    print("Calculation options" + "\n" + "-------------------")
    print("1. Height")
    print("2. Distance")
    print("3. Range")

    calculation = input("Which would you like to calculate? (1, 2, etc.): ")

    return position(calculation)

def position(calculation):
    v0 = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter initial launch angle (degrees): "))
    time = float(input("Enter the total time: "))
    # convert degrees to radians, solve for x and y (position)
    radians = np.radians(angle)

    # time array for graphing
    t_vals = np.linspace(0, time, 50)

    initial_x = v0 * np.cos(radians) * t_vals
    initial_y = v0 * np.sin(radians) * t_vals + 0.5 * g * t_vals ** 2

    if calculation == "1":
        print("Final Height: ", initial_y[-1])
        new_calc = input("Would you like to perform another calculation? (Y/N): ")
        if new_calc == "Y" or new_calc == "y":
            choices()
    elif calculation == "2":
        print("Final Distance: ", initial_x[-1])
        new_calc = input("Would you like to perform another calculation? (Y/N): ")
        if new_calc == "Y" or new_calc == "y":
            choices()
    elif calculation == "3":
        print("Final Position: ", initial_x[-1], " , ", initial_y[-1])

    return v0, angle