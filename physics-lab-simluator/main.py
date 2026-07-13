from Inputs import projectile_math as pm
from Inputs.projectile_math import Projectile
from visualization import graphing as gp
from analysis import csv_io as ci

def main():
    projectile = None

    while True:
        print("Physics Lab Simulator\n---------------------")
        print("1. Projectile calculator")
        print("2. Graph projectile trajectory")
        print("3. Analyze lab data")
        print("4. Exit")

        option = input("Choose an option (1, 2, etc.): ")

        if option == "1":
            projectile = pm.user_input()
        # ensures graph has x and y coordinates to plot
        elif option == "2":
            if projectile is None:
                print("Run the calculator first!")
            else:
                gp.user_choice(projectile)
        elif option == "4":
            print("Goodbye!")
            break

        elif option == "3":
            if projectile is None:
                print("Run the calculator, graph, and simulation first!")
            else:
                filename = input("Enter CSV filename: ")
                ci.save_data(filename, projectile)

    return 0

if __name__ == "__main__":
    exit_code = main()