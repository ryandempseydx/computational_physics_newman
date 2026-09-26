"""
Exercise 3.4: 3D Crystal Lattice Graphics (Newman p.114)
This script uses VPython to render two crystal structures. Part (a) visualizes the alternating ionic lattice 
of Sodium Chloride (NaCl). Part (b) visualizes a Face-Centered Cubic (FCC) metallic lattice.The script also
serves as practice for a professional workflow with coding best practices and version control.

Author: Ryan Dempsey
Date: September 26, 2026
"""

from vpython import sphere, color, vector, canvas

def NaCl_lattice():
    """
    Part (a): creates interactive 3D graphic of a sodium chloride lattice using nested loops to position spheres
    representing sodium (cyan) and chloride (purple) in the appropriate alternating coordinate locations.
    """

    canvas(title="Part (a): Sodium Chloride (NaCl) Ionic Lattice", width=800, height=600)

    # Set sphere and lattice parameters
    L = 3
    R = 0.3
    coordinate_range = range(-L, L + 1)

    # Nested loops sweep through coordinate range and assign each position to Na or Cl based on parity check
    for i in coordinate_range:
        for j in coordinate_range:
            for k in coordinate_range:

                if (i + j + k) % 2 == 0:
                    sphere(radius=R, pos=vector(i, j, k), color=color.cyan)
                else:
                    sphere(radius=R, pos=vector(i, j, k), color=color.purple)

def ffc_lattice():
    """
    Part (b): Created a 3D graphic of a face-centered cubic (FCC) lattice where spheres are positioned at the 
    center of each cubic face, not just the corners.
    """

    canvas(title="Part (b): Face-Centered Cubic (FCC) Metallic Lattic", width=800, height=600)

    # Sphere and lattice parameters
    L = 2
    R = 0.2
    coordinate_range = range(-L, L + 1)

    # Nested loop sweeps through coordinate range of cube
    for i in coordinate_range:
        for j in coordinate_range:
            for k in coordinate_range:
                # Corners of cube
                sphere(radius=R, pos=vector(i, j, k), color=color.cyan)

                # Boundary check prevents face spheres from exceeding cube as defined by corner spheres
                if i < L and j < L and k < L:
                    # Front face of cube
                    sphere(radius=R, pos=vector(i + 0.5, j + 0.5, k))
                    # Bottom face of the cube
                    sphere(radius=R, pos=vector(i + 0.5, j, k + 0.5))
                    # Left face of cube
                    sphere(radius=R, pos=vector(i, j + 0.5, k + 0.5))
                    # Geometric Boundary Closures
                    if i == L - 1:
                        # Right face of cube
                        sphere(radius=R, pos=vector(i + 1, j + 0.5, k + 0.5))
                    if j == L - 1:
                        # Top face of cube
                        sphere(radius=R, pos=vector(i + 0.5, j + 1, k + 0.5))
                    if k == L - 1:
                        # Back face of cube
                        sphere(radius=R, pos=vector(i + 0.5, j + 0.5, k + 1))


if __name__ == "__main__":
    NaCl_lattice()
    ffc_lattice()
    # Create input prompt to keep visualization from closing immediately after opening
    input("Press enter to close visualization.")



   
