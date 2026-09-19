"""
Exercise 2.10: The Semi-Emperical Mass Formula (Newman p.75)
This script utilizes the semi-emperical mass formula to calculate the approximate nuclear binding
energy B and nuclear binding energy per nucleon of an atomic nucleus of with atomic number Z and mass
number A. It also contains a function that takes in an atomic number Z and prints which value of mass
number A yields the highest binding energy per nucleon. A final function runs through the first 100 
elements on the periodic tables and locates the isotope with the highest binding energy. The script also 
serves as practice for a professional workflow with coding best practices and version control.


Author: Ryan Dempsey
Date: September 17, 2024
"""

import numpy as np

# Define function for core mathematical calculation
def calculate_binding_energy(Z, A):

    """
    Core Mathematical Engine: Computes total binding energy (B) and binding energy per nucleon (B/A)
    using the Liquid Drop Model.
    """

    # Define constants for semi empirical mass formula (MeV)
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    if A % 2 != 0:
        a5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a5 = 12
    else:
        a5 = -12

    # Calculating binding energy with semi-emperical mass formula (MeV)
    term_volume = a1 * A
    term_surface = -1 * a2 * (A ** (2 / 3))
    term_coulomb = -1 * a3 * (Z ** 2) / (A ** (1 / 3))
    term_asymmetry = -1 * a4 * ((A - 2 * Z) ** 2) / A
    term_pairing = a5 / (A ** (1 / 2))
    B = term_volume + term_surface + term_coulomb + term_asymmetry + term_pairing
    B_per_nucleon = B / A 

    return B, B_per_nucleon 

def run_parts_a_and_b():
    """
    Executes Parts (a) and (b): Validates user inputs for a single isotope
    and prints out its raw binding energy properties.
    """

    print("\n===Running parts (a) and (b): Single Isotope Evaluation===")

    # Input Parameters using while loop to guarantee correct range of values
    while True:
        Z = int(input("Input atomic number Z (1-118): "))
        if 1 <= Z <= 118:
            break
        print("\nAtomic number must be between 1 and 118!")
    while True:
        A = int(input("Input mass number A: "))
        if A >= Z:
            break
        print("\nMass number must be equal to or greater than atomic number Z!")

    B, B_per_nucleon = calculate_binding_energy(Z, A)

    # Terminal Output Formatting
    print("\n" + "-" * 50)
    print(f"The nuclear binding energy of an atom with A={A} and Z={Z} is {B:,.2f} MeV.")
    print(f"The binding energy per nucleon is {B_per_nucleon:.2f} MeV.")
    print("-" * 50)

def run_part_c():
    """
    Executes Part (c): Sweeps through all physically viable mass numbers A 
    for a user-specified atomic number Z to identify the most stable isotope.
    """

    print("\n===Running part (c): Local Isotope Stability Optimization===")

    # Input parameter Z
    while True:
        Z = int(input("Input atomic number Z (1-118): "))
        if 1 <= Z <= 118:
            break
        print("\nAtomic number Z must be between 1 and 118!")

    A_range = range(Z, 3 * Z + 1)
    max_energy = -np.inf
    best_A = 0

    # High score tracker pattern
    for A in A_range:
        _, B_per_nucleon = calculate_binding_energy(Z, A)
        if B_per_nucleon > max_energy:
            max_energy = B_per_nucleon
            best_A = A 

    #Terminal Output Formatting
    print("\n" + "-" * 50)
    print(f"The most stable nucleus occurs with a mass number A={best_A}.")
    print(f"The binding energy per nucleon is {max_energy:.2f} MeV")
    print("-" * 50)

def run_part_d():
    """
    Executes Part (d): Runs a nested multi-dimensional matrix sweep across 
    atomic numbers Z from 1 to 100 and mass numbers A to discover the 
    absolute most stable nucleus in the periodic table.
    """

    print("\n===Running part (d): Global periodic table matrix scan===")

    # Establish global tracking variables
    global_max_energy = -np.inf
    global_best_Z = 0
    global_best_A = 0

    # Outer loop: sweeps atomic numbers 1-100
    for Z in range(1, 101):

        # Reset local tracking variables at start of each new Z shell
        local_max_energy = -np.inf
        local_best_A = 0

        # Inner loop: sweeps physically viable mass numbers for each Z
        A_range = range(Z, 3 * Z + 1)
        for A in A_range:
            _, B_per_nucleon = calculate_binding_energy(Z, A)

            # Local optimization check
            if B_per_nucleon > local_max_energy:
                local_max_energy = B_per_nucleon
                local_best_A = A 

        # Global optimization check       
        if local_max_energy > global_max_energy:
            global_max_energy = local_max_energy
            global_best_A = local_best_A
            global_best_Z = Z 

    # Terminal Output Formatting   
    print("\n" + "-" * 50)
    print(f"The most stable isotope in the periodic table has values Z={global_best_Z} and A={global_best_A}")
    print("-" * 50)  

if __name__ == "__main__":
    run_parts_a_and_b()
    run_part_c()
    run_part_d()