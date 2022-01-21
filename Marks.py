import csv
import numpy as np

def getDataSource(data_path):
    marks=[]
    daysPresent=[]
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {"x": marks, "y": daysPresent}

def findCorrelation(data_source):
        correlation=np.corrcoef(data_source["x"], data_source["y"])
        print("Correlation: ", correlation[0, 1])

def setUp():
        data_path="Marks.csv"
        data_source=getDataSource(data_path)
        findCorrelation(data_source)

setUp()