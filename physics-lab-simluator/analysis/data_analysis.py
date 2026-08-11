import pandas as pd

class Analysis:
    def __init__(self, data):
        self.max_height = "y"
        self.total_distance = "x"
        self.data = data

        self.calculate_statistics()

    def calculate_statistics(self):
        df = pd.DataFrame(self.data)

        self.max_height = df["y"].max()
        self.total_distance = df["x"].max()

    #def compare_trajectories(self):
        #print("w")

    #def calculate_rmse(self):
        #print("q")