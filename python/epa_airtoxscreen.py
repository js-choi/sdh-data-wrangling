import pandas as pd
import glob

# Specify the pattern for matching files
# pattern = 'data/epa-airtoxscreen/*_Cancer_Risk_in_a_million_and_Noncancer_Risk_hazard_quotient.csv'
pattern = 'data/epa-airtoxscreen/*_Exposure_Concentration_ug_m3.csv'

# Find all files matching the pattern
files = glob.glob(pattern)

# Create an empty list to store DataFrames
dfs = []

# Loop through each file and read it into a DataFrame
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into a single one
merged_df = pd.concat(dfs, ignore_index=True)

# Specify the path for the output CSV file
output_file = 'merged_output.csv'

# Write the merged DataFrame to a CSV file
merged_df.to_csv(output_file, index=False)

print(f"Data written to '{output_file}' successfully.")
