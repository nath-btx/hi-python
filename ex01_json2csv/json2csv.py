import json
import csv
import sys
import pandas as pd

def json2csv(filename):
    data = pd.read_json(filename)
    return data.to_csv()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json2csv(sys.argv[1]))
    else: 
        print('Please select a file')