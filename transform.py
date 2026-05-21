import pandas as pd
import os

def transform_data():
    df = pd.read_csv("data/clean/events.csv")
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")
    
    # Force creation of the directory structure if deleted
    os.makedirs("data/transformed", exist_ok=True)
    df.to_csv("data/transformed/events.csv", index=False)

if __name__ == "__main__":
    transform_data()