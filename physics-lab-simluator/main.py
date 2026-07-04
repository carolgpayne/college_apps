import projectile_math as pm
import graphing as gp
import csv_io as ci

def main():
    v0 = None
    angle = None
    x_points = None
    y_points = None
    t_points = None

    while True:
        print("Physics Lab Simulator\n---------------------")
        print("1. Projectile calculator")
        print("2. Graph projectile trajectory")
        print("3. Analyze lab data")
        print("4. Exit")

        option = input("Choose an option (1, 2, etc.): ")

        if option == "1":
            t_points, x_points, y_points, v0, angle = pm.user_input()

        # ensures graph has x and y coordinates to plot
        elif option == "2":
            if v0 is None or angle is None or x_points is None or y_points is None:
                print("Run the calculator first!")
            else:
                gp.user_choice(x_points, y_points, v0, angle)
        elif option == "4":
            print("Goodbye!")
            break

        elif option == "3":
            if v0 is None or angle is None or t_points is None:
                print("Run the calculator, graph, and simulation first!")
            else:
                filename = input("Enter CSV filename: ")
                ci.save_data(filename, t_points, x_points, y_points)

    return 0

if __name__ == "__main__":
    exit_code = main()