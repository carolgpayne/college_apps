from Calculations import graphing as gp, projectile_math as pm
from simulations import projectile_sim as ps


def main():
    v0 = None
    angle = None

    while True:
        print("Physics Lab Simulator" + "\n" + "---------------------")
        print("1. Projectile calculator")
        print("2. Graph projectile trajectory")
        print("3. Analyze lab data")
        print("4. Exit")

        option = input("Choose an option (1, 2, etc.): ")

        if option == "1":
            v0, angle = pm.choices()

        # ensures graph has x and y coordinates to plot
        elif option == "2":
            if v0 is None or angle is None:
                print("Run the calculator first!")
            else:
                gp.user_choice(0, 0, v0, angle)
        elif option == "4":
            print("Goodbye!")
            break

    return 0

if __name__ == "__main__":
    exit_code = main()