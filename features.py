import pandas as pd

def extract_features():
    # Read transformed data
    df = pd.read_csv("data/transformed/events.csv")
    
    # 1. Calculate duration_minutes
    df["duration_minutes"] = df["duration_seconds"] / 60.0
    
    # 2. Calculate weekday (written in full: Monday, Tuesday, etc.)
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()
    
    # Save final pipeline output
    df.to_csv("data/features/events.csv", index=False)

if __name__ == "__main__":
    extract_features()