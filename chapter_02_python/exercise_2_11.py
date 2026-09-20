"""
Exercise 2.11: Binomial Coefficients (Newman p.82)
This script calculates binomial coefficients (n choose k) and uses them to print the first 20 
rows of Pascal's triangle. The script also serves as practice for a professional workflow with 
coding best practices and version control.

Author: Ryan Dempsey
Date: September 19, 2026
"""


def factorial(f):
    """
    Calculates the factorial of an integer f safely using a loop.
    """
    fact = 1
    for i in range(1, f + 1):
          fact *= i
    return fact


def binomial(n, k):
    """
    Part (a): Calculates the pure integer binomial coefficient (n choose k).
    """
    # Guard clauses for value ranges
    if k < 0 or n < 0:
         return 0
    if k > n:
         return 0
    if k == 0:
         return 1
    
    numerator = factorial(n)
    denom_1 = factorial(k)
    denom_2 = factorial(n -k)
    BINOMIAL_CO = numerator // (denom_1 * denom_2) 

    return BINOMIAL_CO


def run_part_b():
    """
    Executes Part (b): Constructs visual grid of Pascal's triangle 20 rows high.
    """

    print("\n---Running Part (b): Pascal's Triangle---")

    # Nested loop with outer shell tracking n and inner shell tracking k
    for row in range(20):
        for col in range(row + 1):
            tri_value = binomial(row, col)
            print(tri_value, end=" ")
        print()


def run_part_c():
    """
    Executes part (c): Calculates the odds of a coin flipped 100 times coming up heads exactly 60
    times. Then, for the same number of tosses, calculates odds of heads coming up 60 times or more.
    """

    print("\n---Running Part (c): 100 Coin Flips: 60 Heads Exactly and 60 or More---")

    # Calculates # arrangements with 60 heads divided by total state space 
    exact = binomial(100, 60) / 2 ** 100
    odds_sum = 0

    # Loop sweeps through values of k 60-100 to sum up total # arrangements with heads
    for k in range(60, 101):
        odds_sum += binomial(100, k)
    sixty_plus = odds_sum / 2 ** 100

    # Terminal Output Formatting
    print("\n" + "-" * 50)
    print(f"100 Coin Flips: The odds of exactly 60 heads are {exact * 100:.2f}%.")
    print(f"The odds of 60 heads or more are {sixty_plus * 100:.2f}%.")
    print("-" * 50)

    
if __name__ == "__main__":

    # Input Parameters taken outside function to maintain parameter scoping
    while True:
        n_input= int(input("Input value of n: "))
        if n_input >= 0:
              break
        print("\nValue of n must be greater than or equal to !")
    while True:
         k_input = int(input("Input value of k: "))
         if k_input >= 0:
              break
         print("\nValue of k must be between 0 and n!")

    result = binomial(n_input, k_input) 

    # Terminal Output Formatting
    print("\n" + "-" * 50)
    print(f"The binomial coefficient ({n_input}) choose ({k_input}) is: {result}")
    print("-" * 50)

    run_part_b()
    run_part_c()

    

