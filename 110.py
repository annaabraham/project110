import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)

def showfig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomSetOfMean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print(mean)
setup()
populationMean=statistics.mean(data)
print(populationMean)
