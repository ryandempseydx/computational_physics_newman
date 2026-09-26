"""
Exercise 3.3: Scanning Tunneling Microscope Density Plot (Newman p.111)
This script loads raw data from a .txt file containing relative height measurements of an arrangement of silicon 
atoms from a scanning tunneling microscope. It then creates a 2D density plot that provides visual clarity of
the silicon atoms physical arrangement in space with a color scheme that represents relative elevation and 3D
texture and a color bar for reference. The script also serves as practice for a professional workflow with coding
best practices and version control.

Author: Ryan Dempsey
Date: September 25, 2026
"""

import numpy as np
import matplotlib.pyplot as plt


def stm_density_plot():
    """
    Loads stm.txt scanning tunneling microscope data and displays it as a 2D density plot 
    """

    # Load data into 2D array
    data = np.loadtxt("stm.txt")

    plt.figure(figsize=(7, 6))
    # Create density plot from 2D data array. origin="lower" flips y axis to standard cartesian direction
    plt.imshow(data, origin="lower", cmap="copper")
    plt.xlabel("Grid Position ($x$)")
    plt.ylabel("Grid Position ($y$)")
    plt.title("Scanning Tunneling Microscope: Silicon")
    # Add color bar as visual reference for relative elevation scale
    cbar = plt.colorbar()
    cbar.set_label("Relative Height (Arbitrary Units)", rotation=270, labelpad=15)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    stm_density_plot()