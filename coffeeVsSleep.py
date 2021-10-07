from numpy import DataSource, core
import plotly.express as px
import csv
import numpy as np

with open("data\cups of coffee vs hours of sleep.csv") as csvFile:
      df = csv.DictReader(csvFile)
      fig = px.scatter(df, x="week", y="Coffee in ml")
      

def getDataSource(dataPath):
      iceCreamSales = []
      temprature = []
      with open(dataPath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for row in csvReader:
                  temprature.append(float(row["week"]))
                  iceCreamSales.append(float(row["Coffee in ml"]))
      
      return{"x":temprature, "y": iceCreamSales}

def findCoRelation(dataSource):
      coRelation = np.corrcoef(dataSource["x"], dataSource["y"])
      print("Co-relation between temperature and ice cream sales is: ", coRelation[0,1])

def setup():
      dataPath = "./data/iceCream.csv"
      DataSource = getDataSource(dataPath)
      findCoRelation(DataSource)

setup()