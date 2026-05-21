import pandas as pd
import os

def clean_data():
    df = pd.read_csv("data/raw/events.csv")
    
    # 1. Drop rows with any missing fields
    df = df.dropna()
    
    # 2. Strict type conversion: convert duration_seconds to numeric, drop bad formats, and force to integer
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna()  # Remove rows that failed numeric conversion
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int) # Enforce strict integer type
    
    # 3. Explicitly filter out invalid event types
    valid_events = {'click', 'login', 'purchase', 'scroll', 'view'}
    df = df[df["event_type"].isin(valid_events)]
    
    # 4. Normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS) using mixed format parsing
    df["timestamp"] = pd.to_datetime(df["timestamp"], format='mixed').dt.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Force creation of the directory structure if deleted
    os.makedirs("data/clean", exist_ok=True)
    df.to_csv("data/clean/events.csv", index=False)

if __name__ == "__main__":
    clean_data()