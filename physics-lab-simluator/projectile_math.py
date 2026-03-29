# equations: x = v*cos(θ)*t, y = v*sin(θ)*t - 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = 9.81

def choices():
    initial_velocity = 0.0
    launch_angle = 0.0
    time = 0.0

    print("Calculation options" + "\n" + "---------")
    print("1. Height")
    print("2. Distance")
    print("3. Range")
    calculation = input("Which would you like to calculate? (1, 2, etc.): ")

    if calculation == "1" or "2":
        position(initial_velocity, launch_angle, time, calculation)

def position(initial_velocity, launch_angle, time, calculation):
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    launch_angle = float(input("Enter initial launch angle (degrees): "))
    time = float(input("Enter the total time: "))
    # convert degrees to radians, solve for x and y (position)
    radians = np.radians(launch_angle)

    if calculation == "1":
        y = initial_velocity * np.sin(radians) * time + 0.5 * g * time ** 2
        print("Height: ", y)
    if calculation == "2":
        x = initial_velocity * np.cos(radians) * time
        print("Distance: ", x)

