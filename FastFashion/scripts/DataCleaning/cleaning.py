import pandas as pd

def convertNumericToNan(data):
    pd.to_numeric(data["cotton"], errors='coerce').notnull()
    # for columnName in data.columns:
    #      data[pd.to_numeric(data[columnName], errors='coerce')]
    
    print(data.head(20))