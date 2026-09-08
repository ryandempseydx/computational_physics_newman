"""
Exercise 2.4: Distance and Time at relativistic speeds. Newman p.36 
This script calculates the length of journey for a spacecraft traveling from Earth at relativistic 
speeds, at a given percentage of lightspeed, to a destination a given number of lightyears away. It 
is also written as practice for certain professional coding best practices.

Author: Ryan Dempsey
Date: September 7, 2026
"""

import numpy as np 

def calc_time():

    # Input Parameters
    beta = float(input("Enter fraction of lightspeed: ")) 
    x = float(input("Enter distance to destination in lightyears: ")) 

    # Calculate Time of journey with special relativity
    gamma = 1 / np.sqrt(1 - beta**2)
    time_earth = x / beta
    time_ship = time_earth / gamma 

    #Terminal output formatting
    print("\n" + "-"*50)
    print(f"From the reference frame of Earth, the journey will take {time_earth:,.2f} years.")
    print(f"For those aboard the ship, the journey will take {time_ship:,.2f} years")
    print("-"*50)

if __name__ == "__main__":
    calc_time()