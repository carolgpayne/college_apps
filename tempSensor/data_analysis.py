import numpy as np

def import_data():
    data = np.loadtxt("tempSensor.csv", delimiter=",")

    times = data[:, 0]
    temperatures = data[:, 1]

    print(*temperatures)
