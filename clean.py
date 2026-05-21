import pandas as pd
import os

def clean_data():
    df = pd.read_csv("data/raw/events.csv")
    df = df.dropna()
    df = df[df["duration_seconds"] > 0]
    df = df[df["event_type"].astype(str).str.strip() != ""]
    df["timestamp"] = pd.to_datetime(df["timestamp"], format='mixed').dt.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Force creation of the directory structure if deleted
    os.makedirs("data/clean", exist_ok=True)
    df.to_csv("data/clean/events.csv", index=False)

if __name__ == "__main__":
    clean_data()