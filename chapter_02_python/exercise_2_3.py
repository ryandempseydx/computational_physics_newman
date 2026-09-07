"""
Exercise 2.3: Converting Cartesian Coordinates to Polar. Newman p.35

This script takes in a set of coordinates in Cartesian (rectangular) coordinates and converts 
those coordinates to polar form. It is also written as practice for certain professional coding best 
practices. 

Author: Ryan Dempsey
Date: September 7, 2026
"""

import numpy as np

def convert_polar():

    # Input Coordinates
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    # Calculate Polar Coordinates
    r = np.sqrt(x**2 + y**2)
    theta_rad = np.arctan2(y, x)

   
    # Convert theta to degrees -180 to 180 deg
    theta_deg = np.degrees(theta_rad)

    # Shift range to 0-360 deg
    if theta_deg < 0:
        theta_deg += 360.0

    # Terminal Output Formatting
    print("\n" + "-"*50)
    print(f"Your coordinates are r: {r:.2f} theta: {theta_deg:.2f} degrees")
    print("-"*50)

if __name__ == "__main__":
    convert_polar()