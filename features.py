import pandas as pd
import os

def extract_features():
    df = pd.read_csv("data/transformed/events.csv")
    df["duration_minutes"] = df["duration_seconds"] / 60.0
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()
    
    # Force creation of the directory structure if deleted
    os.makedirs("data/features", exist_ok=True)
    df.to_csv("data/features/events.csv", index=False)

if __name__ == "__main__":
    extract_features()