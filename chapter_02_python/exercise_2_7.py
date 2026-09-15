"""
Exercise 2.7: Catalan Numbers (Newman p.46)
This script calculates and prints all Catalan numberes less than one billion. It utilizes 
exact integer arithmetic to prevent floating-point precision loss. It also serves
as practice for certain professional coding best practices.

Author: Ryan Dempsey
Date: September 15, 2026
"""

def catalan_numbers():

    # Set initial parameters for sequence 
    n = 0
    C_n = 1

    # Print first Catalan number
    print(C_n) 

    # Calculate each Catalan number for each value of n until exceeds one billion
    while True:

        # Perform mult. before div. to avoid float precision errors
        C_next = (C_n * (4 * n + 2)) // (n + 2)

        # Guard to break loop when 1e9 is exceeded
        if C_next >= 1e9:
            break

        C_n = C_next     
        print(int(C_n))
        n += 1

if __name__ == "__main__":
        catalan_numbers()