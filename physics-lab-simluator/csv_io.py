import csv

def save_data(filename, t_points, x_points, y_points):
    headers = ["time", "x", "y"]

    with open(filename, "w", newline="", encoding = "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        for i in range(len(t_points)):
            writer.writerow({
                "time": round(t_points[i], 3),
                "x": round(x_points[i], 3),
                "y": round(y_points[i], 3)
            })

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