import pandas as pd

# Step 1: Load the CSV safely
df = pd.read_csv("Airbnb_Open_Data.csv", low_memory=False)

# Step 2: Identify column 25's name
column_25_name = df.columns[25]
print("Cleaning column:", column_25_name)

# Step 3: Convert values to numeric; invalid ones become NaN
df[column_25_name] = pd.to_numeric(df[column_25_name], errors='coerce')

# Step 4: Optionally fill NaN with 0 (or any placeholder)
df[column_25_name] = df[column_25_name].fillna(0)

# Step 5: Save the cleaned version
df.to_csv("Cleaned_Airbnb_Open_Data.csv", index=False)
print("Cleaning done. File saved as 'Cleaned_Airbnb_Open_Data.csv'")
