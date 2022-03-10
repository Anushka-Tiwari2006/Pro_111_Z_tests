import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["id"].to_list()

mean_of_population = statistics.mean(data)
print(mean_of_population)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["id"],show_hist=False)
    fig.show()

mean_list = []
def setup():
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
        show_figure(mean_list)

setup()
mean = statistics.mean(mean_list)
std_dev = statistics.stdev(mean_list)

first_std_dev_start,first_std_dev_end = mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end = mean-(2*std_dev),mean+(2*std_dev)
third_std_dev_start,third_std_dev_end = mean-(3*std_dev),mean+(3*std_dev)

print(first_std_dev_start,first_std_dev_end)
print(second_std_dev_start,second_std_dev_end)
print(third_std_dev_start,third_std_dev_end)

fig = ff.create_distplot([mean_list],["Math_score"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x = [first_std_dev_start,first_std_dev_start], y = [0,0.20],mode = "lines",name = "Stdev 1 first"))
fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.20],mode = "lines",name = "Stdev 1 end"))
fig.add_trace(go.Scatter(x = [second_std_dev_start,second_std_dev_start], y = [0,0.20],mode = "lines",name = "Stdev 2 first"))
fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end], y = [0,0.20],mode = "lines",name = "Stdev 2 end"))
fig.add_trace(go.Scatter(x = [third_std_dev_start,third_std_dev_start], y = [0,0.20],mode = "lines",name = "Stdev 3 first"))
fig.add_trace(go.Scatter(x = [third_std_dev_end,third_std_dev_end], y = [0,0.20],mode = "lines",name = "Stdev 3 end"))






