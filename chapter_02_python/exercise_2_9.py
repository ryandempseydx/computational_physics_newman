"""
Exercise 2.9: Calculating The Madelung Constant (Newman p.74)
This script calculates the Madelung constant used in determining the total electric potential
felt by a sodium atom at the center of a sodium chloride lattice. It is also written as practice for
certain professional coding best practices.

Author: Ryan Dempsey
Date: September 16, 2026
"""

import numpy as np

def madelung_const():

    # Define boundaries of cubic lattice
    L = 30
    coordinate_range = range(-L, L + 1)

    MADELUNG_sum = 0

    # Nested three independent tracking variables to sweep 3D grid
    for i in coordinate_range:
        for j in coordinate_range:
            for k in coordinate_range:

                # Guard clause to skip origin
                if i == 0 and j ==0 and k == 0:
                    continue 

                # Calculate spatial distance denominator
                denominator = np.sqrt(i**2 + j**2 + k**2) 

                # Determine alternating sign for neg and pos charges
                if (i + j + k) % 2 == 0:
                    sign = 1
                else:
                    sign = -1

                # Add potential term to running sum of Madelung constant
                MADELUNG_sum += sign / denominator

    # Terminal Output Formatting 
    print(f"Calculated Madelung Constant (L = {L}): {abs(MADELUNG_sum):.4f}")

if __name__ == "__main__":
    madelung_const()
