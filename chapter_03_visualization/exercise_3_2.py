"""
Exercise 3.2: Curve Plotting (Newman p.98)

Author: Ryan Dempsey
Date: September  25, 2026
"""

import numpy as np
import matplotlib.pyplot as plt


def deltoid_curve():
    """
    Plots a deltoid curve over the domain 0 <= theta < 2*pi.
    """

    # Vectorized array of theta values with parametric definition of x and y
    theta = np.linspace(0, 2 * np.pi, 100)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)

    # Graphic formatting
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("The Deltoid Curve")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axis("equal")


def galilean_spiral():
    """
    Plots the Galilean Spiral (r = theta^2) projected into Cartesian coordinates
    over the domain 0 <= theta <= 10*pi (5 full rotations).
    """

    # Vectorized array of theta values for polar function r=f(theta) where r is parameter for x and y
    theta = np.linspace(0, 10 * np.pi, 1000)
    r = theta ** 2
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Graphic formatting
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.title("The Galilean Spiral")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axis("equal")


def feys_function():
    """
    Plots Fey's Function (The Butterfly Curve) in Cartesian coordinates
    over the domain 0 <= theta <= 24*pi (12 full rotations).
    """

    # Vectorized array for polar parametric function r=f(theta). Converted to cartesian coordinates
    theta = np.linspace(0, 24 * np.pi, 2400)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 12) ** 5
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Graphic formatting
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.title("Fey's Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.axis("equal")

    
if __name__ == "__main__":
    deltoid_curve()
    galilean_spiral()
    feys_function()

    plt.show()