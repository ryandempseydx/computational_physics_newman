"""
Exercise 2.13: Recursive Functions  (Newman p.84)
This script features two recursive functions that implement two mathematical sequences: the exact integer
generation of Catalan numbers and Euclid's algorithmic method for finding the Greatest Common Divisor (GCD).
The script also serves as practice for a professional workflow with coding best practices and version control.

Author: Ryan Dempsey
Date: September 21, 2026
"""


def catalan(n):
    """
    This function uses a recursive formula to calculate the nth Catalan number.
    """

    # Set base case for recursion.
    if n == 0:
        return 1
    # The resursive step/formula
    else:
        C_n = catalan(n - 1) * (4 * n - 2) // (n + 1)
        return C_n 


def GCD(m, n):
    """
    This function takes in two integers as parameters and returns their greatest common divisor using Euclid's
    recursive parameter rotation.
    """

    # Set base case for recursion
    if n == 0:
        return m
    # Recursive step: rotate parameters using modulo remainder
    else:
        return GCD(n, m % n)

    
if __name__ == "__main__":

    # Part (a): Catalan number for n=100
    cat_100 = catalan(100)
    print("\n" + "-" * 50)
    print(f"The Catalan number for n=100 is {cat_100:,}.")

    # Part (b): Greatest common divisors for integers m=108 n=192
    gcd_108_192 = int(GCD(108, 192))
    print("-" * 50)
    print(f"Greatest common divisor of 108 and 192 is {gcd_108_192}")
    print("-" * 50)

