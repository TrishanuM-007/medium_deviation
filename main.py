import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df["id"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,30):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["id"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y =[0,0.1], mode = "lines", name = "mean" ))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: ",mean)
setup()
def standardDeviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print("stdev of sampling distribution: ",std_deviation)
standardDeviation()



