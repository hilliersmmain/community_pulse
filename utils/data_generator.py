import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_messy_data(num_records=500, save_path=None):
    """
    Generates a dataset with intentional 'messiness' for cleaning demonstration.
    Messiness includes:
    - Duplicates (approx 10%)
    - Inconsistent capitalization in Names
    - Invalid Email formats
    - Inconsistent Date formats (YYYY-MM-DD vs MM/DD/YYYY)
    - Missing values (NaN)
    """
    data = []
    
    # Generate base data
    for _ in range(num_records):
        # Event registration logic
        event_choices = ["Spring Gala", "Summer Camp", "Fall Fundraiser", "None"]
        event_registered = np.random.choice(event_choices, p=[0.25, 0.25, 0.25, 0.25])
        
        # Registration date (only if registered for an event)
        if event_registered != "None" and random.random() > 0.4:
            # 60% of registered users have a registration date
            reg_date = fake.date_between(start_date='-6m', end_date='today')
        else:
            reg_date = None
        
        record = {
            "ID": fake.uuid4(),
            "Name": fake.name(),
            "Email": fake.email(),
            "Join_Date": fake.date_between(start_date='-2y', end_date='today'),
            "Last_Login": fake.date_time_between(start_date='-1y', end_date='now'),
            "Event_Attendance": np.random.randint(0, 20),
            "Role": np.random.choice(["Member", "Admin", "Guest"], p=[0.8, 0.05, 0.15]),
            "Event_Registered": event_registered,
            "Registration_Date": reg_date
        }
        data.append(record)
    
    df = pd.DataFrame(data)
    
    # --- INTRODUCE MESSINESS ---
    
    # 1. Duplicates
    num_duplicates = int(num_records * 0.1)
    duplicates = df.sample(num_duplicates, replace=True)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # 2. Inconsistent Names (mix of UPPER, lower, Title)
    def mess_up_name(name):
        r = random.random()
        if r < 0.1: return name.upper()
        if r < 0.2: return name.lower()
        return name
    df['Name'] = df['Name'].apply(mess_up_name)
    
    # 3. Invalid Emails
    def mess_up_email(email):
        if random.random() < 0.05:
            return email.replace("@", " at ") # Invalid format
        return email
    df['Email'] = df['Email'].apply(mess_up_email)
    
    # 4. Inconsistent Date Formats & Types in 'Join_Date'
    # Current format is datetime.date object. Convert some to strings of different formats.
    def mess_up_date(d):
        r = random.random()
        if r < 0.1:
            return d.strftime("%m/%d/%Y") # US format string
        if r < 0.2:
            return d.strftime("%d-%m-%Y") # Euro format string
        if r < 0.25:
             # Random string noise
            return "Unknown" 
        return d # Keep as object or ISO string roughly
    df['Join_Date'] = df['Join_Date'].apply(mess_up_date)

    # 5. Missing Values
    cols_to_nan = ['Event_Attendance', 'Last_Login']
    for col in cols_to_nan:
        df.loc[df.sample(frac=0.05).index, col] = np.nan

    # Shuffle dataset
    df = df.sample(frac=1).reset_index(drop=True)
    
    if save_path:
        df.to_csv(save_path, index=False)
        print(f"Generated messy data at {save_path} with {len(df)} rows.")
        
    return df

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    import os
    if not os.path.exists("../data"):
        os.makedirs("../data", exist_ok=True)
        
    generate_messy_data(save_path="../data/messy_club_data.csv")
