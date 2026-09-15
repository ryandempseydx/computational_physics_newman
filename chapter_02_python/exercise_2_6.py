"""
Exercise 2.6: Planetary Orbits and Kepler's 2nd Law Newman p.36
This is a script that, given a planet's distance from the sun and velocity at perihelion, 
calculates it's orbital period, eccentricity, and it's distance from the sun and velocity
at aphelion. It is also written as practice for certain professional coding best practices.

Author: Ryan Dempsey
Date: September 14, 2026
"""

import numpy as np 

# Define Constants
M_SUN = 1.9891e30   # Mass Sun (kg)
G = 6.6738e-11      # Graviational Constant (m^3 kg^-1 s^-2)

def orbital_calc():

    # Input Parameters
    r1 = float(input("Enter planet's distance from the Sun in m at perihelion: "))
    v1 = float(input("Enter planet's velocity in m/s at perihelion: "))

    # Calculate velocity (v2)/distance (r1) at aphelion by solving cons. linear momentum polynomial
    b_coeff = -2 * G * M_SUN / (r1 * v1)
    c_coeff = -1 * (v1**2 - (2 * G * M_SUN / r1))
    discriminant = np.sqrt(b_coeff**2 - 4 * c_coeff)
    v2 = (-1 * b_coeff - discriminant) / 2    # Velocity at aphelion (m/s)    
    r2 = r1 * v1 / v2                   # Distance at aphelion (m) 

    # Calculate orbital period (T), eccentricity (e), distance at aphelion (r2)
    a = (r1 + r2) / 2                   # Semi-major axis
    b = np.sqrt(r1 * r2)                # Semi-minor axis
    T = 2 * np.pi * a * b / (r1 * v1)   # Orbital Period (s)
    e = (r2 - r1) / (r1 + r2)           # Orbital eccentricity

    # Terminal Output Formatting
    print("\n" + "-" * 50)
    print(f"At aphelion, the planet is {r2:,.2f} m or {r2 / 1000:,.2f} km from the sun with velocity {v2:,.2f} m/s.")
    print(f"The planet has an orbital period of {T:,.2f} s or {T / 3.15e7:,.2f} years.")
    print(f"The planet's eccentricity of orbit is {e:.2f}.")
    print("-" * 50)

if __name__ == "__main__":
    orbital_calc()