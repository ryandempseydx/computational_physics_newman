"""
Exercise 2.1: Projectile Motion Time Calculator Newman p.30

This script takes in a value for the height of a tower and calculates the length of time it will
take for a ball dropped from rest at the top of the tower to reach the bottom. It is also written
as practice for certain professional coding best practice standards.

Author: Ryan Dempsey
Date: September 5, 2026
"""

import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m s^-2)

def calculate_time():

    # Input parameters
    h = float(input("Enter the height of the tower in meters: "))

    # Safety check for negative heights
    if h < 0:
        print("\nError: Height cannot be negative!")
    else:
        # Kinematic calculation: t = sqrt(2h / g)
        t = np.sqrt((2 * h) / g)
        print(f"\nThe ball will hit the ground after {t:.2f} seconds.")

if __name__ == "__main__":
    calculate_time()