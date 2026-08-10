import csv
from analysis.data_analysis import Analysis

def save_data(filename, projectile):
    headers = ["time", "x", "y"]

    with open(filename, "w", newline="", encoding = "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        for i in range(len(projectile.t_points)):
            writer.writerow({
                "time": round(projectile.t_points[i], 3),
                "x": round(projectile.x_points[i], 3),
                "y": round(projectile.y_points[i], 3)
            })

    load_data(filename)

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

    analysis = Analysis(data)
    analysis.calculate_statistics(data)