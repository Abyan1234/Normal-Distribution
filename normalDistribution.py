import random

import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go 
import pandas as pd

dice_result=[]

df=pd.read_csv("StudentsPerformance.csv")
testScore=(df.groupby("math score").mean())




df=pd.read_csv("StudentsPreformance.csv")

  
mean=testScore
std_deviation=statistics.stdev(testScore)
median=statistics.median(testScore)
mode=statistics.mode(testScore)

first_std_devitation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

print("This is the mean:= ",str(mean))
print("This is the standard deviation:= ",str(std_deviation))
print("This is the median:= ",str(median))
print("This is the mode:= ",str(mode))

fig=go.Figure(go.Scatter(
    x=df.groupby("test scores").mean(),
    y=df["math score"+"reading score"+"writing score"],
    
))

fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_devitation_start,first_std_devitation_start],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 2"))

fig.show()