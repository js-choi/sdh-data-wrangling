import pandas as pd
import os

# Path to the directory containing your CSV files
directory = 'data/USDA_food_access'

# Get list of CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Read each CSV file and concatenate into a single DataFrame
dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(directory, file))
    dfs.append(df)

# Concatenate all DataFrames into a single one
merged_df = pd.concat(dfs, ignore_index=True)

# Path to save the merged CSV file
output_file = 'data/merged/USDA_food_access.csv'

# Save the merged DataFrame to a CSV file
merged_df.to_csv(output_file, index=False)

print("Merged CSV file saved successfully.")
