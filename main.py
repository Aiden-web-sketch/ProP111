import plotly.figure_factory as ff
# import plolty.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("studentMarks.csv")
data=df["z_score"].tolist()


fig=ff.create_distplot([data],["z_score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("mean is ",mean)
print("standered division is", std_deviation)