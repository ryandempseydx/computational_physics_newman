"""
Exercise 2.2: Satellite Altitudes and Orbital Periods with Kepler's 3rd Law (Newman p.30)

This script calculates the altitude a satellite orbits at given its orbital period using Kepler's 
3rd Law. It is also written as practice for certain professional coding best practices.

Author: Ryan Dempsey
Date: 9/6/26
"""

import numpy as np

# Constants (SI)
G = 6.67e-11  # Newton's gravitational constant (m^3 kg^-1 s^-2)
M = 5.97e24   # Mass of Earth (kg)
R = 6.371e6   # Avg radius of Earth (m)


def calculate_altitude():

    # Input parameters
    period = float(input("Enter period of orbit for satellite in seconds: "))

    # Calculation using Kepler's 3rd Law
    numerator = G * M * (period ** 2) 
    denominator = 4 * (np.pi ** 2)
    altitude = np.cbrt(numerator / denominator) - R

    # Terminal output formatting
    print("\n" + "-"*50)
    print(f"Orbital Period: {period:,.2f} seconds")
    print(f"Satellite Altitude: {altitude:,.2f} meters ({altitude / 1000:,.2f} kilometers)")
    print("-"*50)
    

if __name__ == "__main__":
    calculate_altitude()