import pandas as pd
import os

# set the path to the folder containing the CSV files
folder_path = 'C:/Users/20065/Downloads/labpy'

# initialize an empty dataframe to store the merged data
merged_df = pd.DataFrame()

# loop through each CSV file in the folder and append its rows to the merged dataframe
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        merged_df = merged_df.append(df)

# save the merged dataframe as a new CSV file
merged_df.to_csv('C:/Users/20065/Downloads/labpy/imbd_data.csv', index=False)
