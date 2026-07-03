import numpy as np

def import_data():
    data = np.loadtxt("tempSensor.csv", delimiter=",")

    times = data[:, 0]
    temperatures = data[:, 1]

    analyze_data(times, temperatures)


def analyze_data(times, temperatures):
    print(f"Average Temperature: {(sum(temperatures) / len(times)):.2f} °C")
