import pandas as pd

def csv_to_json(url):
    dataframe = pd.read_csv(url,  error_bad_lines=False)
    result = [];
    headers = dataframe.columns.values[0].split(";")
    for i in range(0, dataframe.shape[0]):
         result.append(dataframe.loc[i].item().split(";"))
    return { 'headers': headers, 'body': result }
    