import os
import pandas as pd
import json

# 1. get the .csv file in the directory
file_list = []
for i, j, k in os.walk('.'):
    for file in k:
        if file.endswith('.csv'):
            file_list.append(file)

if not file_list:
    print("Can not find the csv file in the directory.")
else:
    # read data from the csv file
    for filename in file_list:
        # get params for dataset
        csv_data = pd.read_csv(filename)
        row_size = csv_data.shape[0]
        col_size = csv_data.shape[1]
        col_list = csv_data.columns.values
        # store into dict
        after_dic = {}
        for i in range(100):
            temp_dict = {}
            for col_name in col_list:
                content = str(csv_data.iloc[i][col_name]).strip()
                if col_name == 'PostCode':
                    content = str(csv_data.iloc[i][col_name]).strip().split('.')[0]
                temp_dict[col_name] = content
            after_dic[i] = temp_dict
        json_name = filename.split('.')[0] + '.json'
        with open(json_name, 'w') as json_file:
            # make it more readable and pretty
            json_file.write(json.dumps(after_dic, indent=4))
    print('Finish transformation from csv to json file!')
