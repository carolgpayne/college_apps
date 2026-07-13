# equations: x = v*cos(θ)*t, y = v*sin(θ)*t - 0.5*g*t^2 (kinematics 2-D)
import numpy as np

# constants
g = 9.81

def user_input():
    print("Calculation options\n-------------------")
    print("1. Height")
    print("2. Distance")
    print("3. Range")

    calculation = input("Which would you like to calculate? (1, 2, etc.): ")

    v0 = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter initial launch angle (degrees): "))
    time = float(input("Enter the total time: "))

    projectile = Projectile(v0, angle)
    projectile.position(time)
    projectile.display_results(calculation)

    return projectile

class Projectile:
    def __init__(self, v0, angle):
        self.v0 = v0
        self.angle = angle
        self.x_points = []
        self.y_points = []
        self.t_points = []


    def position(self, time):
        # convert degrees to radians, solve for x and y (position)
        radians = np.radians(self.angle)

        t = np.linspace(0, time, 50)

        x = self.v0 * np.cos(radians) * t
        y = self.v0 * np.sin(radians) * t - 0.5 * g * t ** 2

        for i in range(len(t)):
            if y[i] >= 0:
                self.t_points.append(t[i])
                self.x_points.append(x[i])
                self.y_points.append(y[i])
            else:
                break


    def display_results(self, calculation):
        if calculation == "1":
            print(f"Final Height: {self.y_points[-1]:.2f}")
        elif calculation == "2":
                print(f"Final Distance: {self.x_points[-1]:.2f}")
        elif calculation == "3":
            print(f"Final Position: {self.x_points[-1]:.2f} , {self.y_points[-1]:.2f}")
        return None
