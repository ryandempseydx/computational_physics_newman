"""
Exercise 2.5: Quantum Potential Step. Newman p.36
This is a script that calculates the probabilites of trasmission or reflection for a particle of
mass m, kinetic energy E, and wavevector k1 encountering a sudden jump in potential V. It is also 
written as practice for certain professional coding best practices.

Author: Ryan Dempsey
Date: September 13, 2026
"""

import numpy as np 

# Define Constants 
M_ELECTRON = 9.11e-31       # Mass electron (kg)
HBAR = 1.0546e-34           # Planck Constant (J*s)
EV_TO_JOULES = 1.602e-19    # Joules per eV 

def calculate_prob():

    # Input Parameters
    energy_ev = 10 
    v_step_ev = 9 

    # Convert eV to Joules
    energy_joules = energy_ev * EV_TO_JOULES 
    v_step_joules = v_step_ev * EV_TO_JOULES

    # Define wavevector 
    k1 = np.sqrt(2 * M_ELECTRON * energy_joules) / HBAR 
    k2 = np.sqrt(2 * M_ELECTRON * (energy_joules - v_step_joules)) / HBAR

    # Calculate Transmission/Reflection coefficients 

    transmission_t = (4 * k1 * k2) / (k1 + k2) ** 2
    reflection_r = ((k1 - k2)/(k1 + k2)) ** 2

    # Terminal Output Formatting 
    print("\n" + "-" * 50)
    print(f"Transmission Probability (T): {transmission_t:.4f}")
    print(f"Reflection Probability (R): {reflection_r:.4f}")
    print(f"Total Probability (T + R): {transmission_t + reflection_r:.4f}")
    print("-" * 50)


if __name__ == "__main__":
    calculate_prob()