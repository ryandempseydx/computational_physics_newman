import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Input parameters
h = float(input("Enter the height of the tower in meters: "))

# Safety check for negative heights
if h < 0:
    print("\nError: Height cannot be negative!")
else:
    # Kinematic calculation: t = sqrt(2h / g)
    t = np.sqrt((2 * h) / g)
    print(f"\nThe ball will hit the ground after {t:.2f} seconds.")