from sklearn.metrics import mean_squared_error, accuracy_score
import csv

def load_data(filename):
    data = {"time": [],
    "x": [],
    "y": []
    }

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data["time"].append(float(row["time"]))
            data["x"].append(float(row["x"]))
            data["y"].append(float(row["y"]))

    return data