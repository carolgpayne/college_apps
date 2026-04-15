from Calculations import graphing as gp, projectile_math as pm
from simulations import projectile_sim as ps


def main():
    x_vals = None
    y_vals = None

    while True:
        print("Physics Lab Simulator" + "\n" + "---------------------")
        print("1. Projectile calculator")
        print("2. Graph projectile trajectory")
        print("3. Run projectile simulation")
        print("4. Analyze lab data")
        print("5. Exit")

        option = input("Choose an option (1, 2, etc.): ")

        if option == "1":
            x_vals, y_vals = pm.choices()

        elif option == "2":
            if x_vals is None or y_vals is None:
                print("Run the calculator first!")
            else:
                gp.graph_position()
        elif option == "3":
            ps.time(x_vals, y_vals)

        elif option == "5":
            print("Goodbye!")
            break

    return 0

if __name__ == "__main__":
    exit_code = main()