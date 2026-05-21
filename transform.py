import pandas as pd

def transform_data():
    # Read clean data
    df = pd.read_csv("data/clean/events.csv")
    
    # Extract just the date portion (YYYY-MM-DD) from the ISO string
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")
    
    # Save output
    df.to_csv("data/transformed/events.csv", index=False)

if __name__ == "__main__":
    transform_data()