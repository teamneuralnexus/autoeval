#for merging
 
import pandas as pd
 
# Path to your CSV files
file1 = '/home/autoeval/phase1/output1.csv'
file2 = '/home/autoeval/phase1/output2.csv'
 
# Read both CSV files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
 
# Concatenate DataFrames row-wise
merged_df = pd.concat([df1, df2], ignore_index=True)
 
# Path to the output merged CSV file
merged_file = 'final_output.csv'
 
# Write merged DataFrame to CSV
merged_df.to_csv(merged_file, index=False)
 
print(f'Merged data saved to {merged_file}')