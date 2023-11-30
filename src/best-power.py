
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#  dynamic programming approach for constructing best effort power curve: use results of previous calculations for the next iteration
#  example: 
# - store cumulative sums for 2 second intervals in temporary array
# - The 3 second cumulative sums can be calculated by adding preceding 2 second sum, plus the power value at the current index
# - At index 0 in the 2 second interval array, we have the cumulative sum from 0 - 2 seconds. The cumulative sum from 0-3 is the sum from 0-2 plus the power value at 3 seconds.
def getBestEffort(powerStream: list, previous: list): 
        current = []
        j = 0
        max = 0
        for key, value in enumerate(powerStream):
            current.append(value + previous[j])
            j += 1
            if current[key] > max:
                    max = current[key]
        return current, max

def getBestEfforts(powerStream: list) -> list:
    # best efforts array: index corresponds to time interval, value corresponds to the average power value
    bestEfforts = []
    bestEfforts.append(max(powerStream))
    previous = powerStream
    # iterate through time intervals from 2 seconds to duration of activity
    for i in range(len(powerStream) + 1):
        if i > 1:
            current, maxPower = getBestEffort(powerStream[(i -1):], previous)
            bestEfforts.append(maxPower/i)
            previous = current
    return bestEfforts

def get_best_efforts_df(bestEfforts: list) -> pd.DataFrame:
    best_power_df = pd.DataFrame({"power": bestEfforts})
    best_power_df = best_power_df[best_power_df['power'] > 0]
    return best_power_df

df = pd.read_csv('data/ride.csv')

start = timer()
bestEfforts = getBestEfforts(df['power'])
end = timer()

print("Time to calculate best efforts: ", end - start) # Time in seconds, e.g. 5.38091952400282
best_power_df = get_best_efforts_df(bestEfforts)
time = np.arange(0, best_power_df['power'].count())

# x_ticks = 1, 10, 
plt.figure(figsize=(12,8))
sns.lineplot(x=time, y=best_power_df['power'])

plt.title("Power Curve")
plt.xlabel("Time - seconds")
plt.ylabel("Average Power - watts")
plt.savefig('figs/power-curve.png')
