from Calculations import graphing as gp, projectile_math as pm
from simulations import projectile_sim as ps


def main():
    x_vals = None
    y_vals = None
    initial_velocity = None
    launch_angle = None
    total_time = None

    while True:
        print("Physics Lab Simulator" + "\n" + "---------------------")
        print("1. Projectile calculator")
        print("2. Graph projectile trajectory")
        print("3. Run projectile simulation")
        print("4. Analyze lab data")
        print("5. Exit")

        option = input("Choose an option (1, 2, etc.): ")

        if option == "1":
            x_vals, y_vals, initial_velocity, launch_angle, total_time = pm.choices()
            # fix, make it an array?

        elif option == "2":
            if x_vals is None or y_vals is None:
                print("Run the calculator first!")
            else:
                gp.graph_position()
        elif option == "3":
            if initial_velocity is None or y_vals is None or total_time is None:
                print("Run the calculator first!")
            else:
                ps.time(x_vals, y_vals, initial_velocity, launch_angle, total_time)
        elif option == "5":
            print("Goodbye!")
            break

    return 0

if __name__ == "__main__":
    exit_code = main()