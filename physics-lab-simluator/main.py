import projectile_math as pm
import numpy as np
import graphing as gp
from simulations import projectile_sim
import time as tm
import data_loader as dl

def main():
    print("Physics Lab Simulator" + "\n" + "---------------------")
    print("1. Projectile calculator")
    print("2. Graph projectile trajectory")
    print("3. Run projectile simulation")
    print("4. Analyze lab data")
    print("5. Exit")

    option = input("Choose an option (1, 2, etc.): ")

    if option == "1":
        pm.choices()

    return 0

if __name__ == "__main__":
    exit_code = main()