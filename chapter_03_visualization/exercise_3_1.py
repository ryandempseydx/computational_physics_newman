"""
Exercise 3.1: Plotting Experimental Data (Newman p.98)
This script loads historical sunspot data, slices it to analyze the first 1000 months, and uses an 
11 month running average filter to smooth out data revealing the 11-year solar cycle. The script also
serves as practice for a professional workflow with coding best practices and version control.

Author: Ryan Dempsey
Date: September 24, 2026
"""
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    """
    Loads the data from sunspots.txt and separates it by column into time and sunspot arrays
    """
    
    data = np.loadtxt("sunspots.txt")
    time = data[:,0]
    sunspots = data[:,1]

    return time, sunspots


def running_avg(sunspots_sliced, r=5):
    """
    Calculates moving average of sliding (2r +1) month blocks to visually clarify results.
    """

    sunspots_avg = []

    # Loop runs through center positions where full 11 month block avg exists
    for y in range(r, len(sunspots_sliced) - r):
        block = sunspots_sliced[y - r : y + r + 1]
        block_avg = np.sum(block) / (2 * r + 1)
        sunspots_avg.append(block_avg)

    return sunspots_avg

    
def sunspot_time_series():
    """
    Executes parts (a) (b) and (c). Parts (b) and (c) are overlaid against one another on the same graph.
    """
    time, sunspots = load_data()

    # Part (a): graphs the raw data of # sunspots over time in months
    plt.figure(figsize=(10,4))
    plt.plot(time, sunspots, label="Raw Data")
    plt.xlabel("Time (Months)")
    plt.ylabel("Number of Sunspots")
    plt.title("Part (a): Sunspots Recorded Since 1749")
    plt.legend()
    plt.grid(True)

    # Part (b): Slices data down to first 1000 months
    time_sliced = time[:1000]
    sunspots_sliced = sunspots[:1000]
    
    plt.figure(figsize=(10,4))
    plt.plot(time_sliced, sunspots_sliced, label="Raw Monthly Data", color="lightgrey")

    # Part (c): Graphs 11 month running average of sliced data
    sunspots_avg = running_avg(sunspots_sliced, r=5)
    time_avg = time_sliced[5 : len(time_sliced) - 5]

    plt.plot(time_avg, sunspots_avg, label="11 Month Running Avg", color="crimson")
    plt.xlabel("Time (Months)")
    plt.ylabel("Number of Sunspots")
    plt.title("Parts (b) and (c): Sunspots Recorded 1749-1832")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    sunspot_time_series()