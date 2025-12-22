import pandas as pd
import os


data = { 'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age':[25,30,35],
        'City':['Ohio','NY','EMEA']
        }

df= pd.DataFrame(data)


# Adding new row for data V2
new_row_loc= {'Name':'GF','Age':30, 'City':'APAC'}
df.loc[len(df.index)] = new_row_loc
# Adding new row for data V3
# new_row_loc= {'Name':['V3'],'Age':[99], 'City':['NAMER']}


# Ensure data dir is at root
data_dir='data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir , 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV saved to {file_path}")
