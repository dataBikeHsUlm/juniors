import os
import pandas as pd

file_list = list()

os.chdir("../data")

for file in os.listdir():
    df = pd.read_csv(file, sep='\t', header=None, encoding='utf-8', low_memory=False)
    df['filename'] = file
    file_list.append(df)

combined = pd.concat(file_list, axis=0, ignore_index=True)
combined.to_csv('geonames-and-postcodeinfo.csv', sep='\t', index=False, encoding='utf-8', header=False)