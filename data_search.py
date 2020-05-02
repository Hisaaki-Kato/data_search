import os
import glob
import pandas as pd
import numpy as np

def data_read():
    data_list = glob.glob('datasheets/*.xl*')
    return data_list

def data_search(data_list, input_keyword):
    input_keyword = str(input_keyword).upper()
    keywords = input_keyword.split(',')

    output_data_list = {}

    for data in data_list:
        data_name = os.path.basename(data)
        output_data = pd.DataFrame()
        df = pd.read_excel(data)
        df = df.fillna('').astype(str).apply(lambda x: x.str.upper())

        for keyword in keywords:
            df_nan = df.where(df == keyword)
            df_searched = df[df_nan.isnull().all(axis=1) == False]
            output_data = pd.concat([output_data, df_searched], axis=0, sort=False)

        if len(output_data) != 0:
            output_data_list.update([(data_name, output_data)])
    
    return output_data_list
