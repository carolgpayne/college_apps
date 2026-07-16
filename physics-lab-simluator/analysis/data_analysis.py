import pandas as pd

def calculate_statistics(data: object) -> None:
    df = pd.DataFrame(data)

    max_height = df["y"].max()

    print(f"Max Height: {max_height} m")

def compare_trajectories():
    print("w")

def calculate_rmse():
    print("q")