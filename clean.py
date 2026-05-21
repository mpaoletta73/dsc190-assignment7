import pandas as pd

def clean_data():
    # Read raw data
    df = pd.read_csv("data/raw/events.csv")
    
    # 1. Drop rows with any missing fields
    df = df.dropna()
    
    # 2. Drop rows with non-positive duration_seconds
    df = df[df["duration_seconds"] > 0]
    
    # 3. Drop rows with invalid event types (ensuring they are non-empty strings)
    df = df[df["event_type"].astype(str).str.strip() != ""]
    
    # 4. Normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS) using mixed format parsing
    df["timestamp"] = pd.to_datetime(df["timestamp"], format='mixed').dt.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Save output
    df.to_csv("data/clean/events.csv", index=False)

if __name__ == "__main__":
    clean_data()