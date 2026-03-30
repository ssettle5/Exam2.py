# Program Name: Exam2.py
# Course: IT1114/Section 01
# Student Name: Sophia Settle
# Assignment Number: Exam2
# Due Date: 03/29/2026
# Purpose: calculate the total volume of a water tower

import math

# Function to calculate volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Function to calculate volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Main program
sphere_radius = float(input("What is the radius for the sphere portion: "))
cylinder_radius = float(input("What is the radius for the cylinder portion: "))
cylinder_height = float(input("What is the height for the cylinder portion: "))

# Half sphere volume
half_sphere = sphere_volume(sphere_radius) / 2

# Cylinder volume
cylinder = cylinder_volume(cylinder_radius, cylinder_height)

# Total volume
total_volume = half_sphere + cylinder

print("Volume:", total_volume)
