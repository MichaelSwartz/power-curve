
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from time_interval_helper import generate_intervals
from timeit import default_timer as timer
from plot_helpers import plot_run_time
from codewong import findMaxAverage

df = pd.read_csv('data/ride-2.csv')

df = df['power'].dropna()

time_intervals = generate_intervals(df.count())

power = df.to_list()

times = []
bestEfforts = []
for interval in time_intervals:
    start = timer()
    max = findMaxAverage(power, interval)
    end = timer()
    times.append(1000 *(end - start))
    bestEfforts.append(max)

plot_run_time(times, 'Run time - Kadane algorithm with required time intervals', 'figs/run-time-kadane-required-time-intervals.png')

# sns.set_style("whitegrid")
# # plt.xlabel("Time")
# # plt.ylabel("Average Power - watts")
# # plt.savefig('figs/power-curve-v2.png')


# plt.figure(figsize=(12,8))
# sns.lineplot(x=np.arange(0, len(times)), y=times)

# plt.title("Run time - Kadane algorithm with required time intervals", fontsize=14)
# plt.xlabel("Iteration")
# plt.ylabel("Time - milliseconds")
# plt.savefig('figs/run-time-kadane-required-time-intervals.png')

# start = timer()
times = []
bestEfforts = []
for i in range(df.count()):
    if i > 1:
        start = timer()
        max = findMaxAverage(df.to_list(), i)
        end = timer()
        times.append(1000 *(end - start))
        bestEfforts.append(max)

plot_run_time(times, 'Run time - Kadane algorithm', 'figs/run-time-kadane.png')
# end = timer()
# print(bestEfforts)
# print(end - start)


# sns.set_style("whitegrid")
# plt.xlabel("Time")
# plt.ylabel("Average Power - watts")
# plt.savefig('figs/power-curve-v2.png')


# plt.figure(figsize=(12,8))
# sns.lineplot(x=np.arange(0, len(times)), y=times)

# plt.title("Run time - Kadane algorithm", fontsize=14)
# plt.xlabel("Iteration")
# plt.ylabel("Time - milliseconds")
# plt.savefig('figs/run-time-kadane.png')
