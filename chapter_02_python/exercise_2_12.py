"""
Exercise 2.12: Prime Numbers (Newman p.83)
This script finds and prints all prime numbers less than ten thousand. It utilizes a number of innovations to 
drastically improve efficiency of prime number finder: checking division only against previously discovered primes,
capping divisor check at the square root of the target number, and exiting the loop immediately upon finding a 
factor. The script also serves as practice for a professional workflow with coding best practices and version
control.

Author: Ryan Dempsey
Date: September 20, 2026
"""

import numpy as np


def prime_numbers():

    # Initialize list of primes starting at 2
    primes = [2]

    # Outer loop runs through tracking variable n up to 10k
    for n in range(3, 10000):
        # Use status flag to verify prime or not
        is_prime = True
        for p in primes:
            # If prime excceeds sqrt(n), no smaller factor pair can exist
            if p > np.sqrt(n):
                break
            # Exit loop if prime factor discovered
            if n % p == 0:
                is_prime = False
        # Update prime list 
        if is_prime == True:
            primes.append(n)
        
    print(primes)


if __name__ == "__main__":
    prime_numbers()