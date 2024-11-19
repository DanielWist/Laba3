import math
import random

def main():
    n = int(input("Enter the number of points: "))

    cartesian_coords = [[0] * 2 for _ in range(n)] 
    polar_coords = [[0] * 2 for _ in range(n)] 

    for i in range(n):
        radius = random.random() * 10
        angle_in_degrees = random.random() * 360
        angle_in_radians = math.radians(angle_in_degrees)

        x = radius * math.cos(angle_in_radians)
        y = radius * math.sin(angle_in_radians)

        polar_coords[i][0] = radius
        polar_coords[i][1] = angle_in_degrees
        cartesian_coords[i][0] = x
        cartesian_coords[i][1] = y

    for i in range(n):
        radius = math.sqrt(cartesian_coords[i][0] ** 2 + cartesian_coords[i][1] ** 2)
        angle = math.degrees(math.atan2(cartesian_coords[i][1], cartesian_coords[i][0]))

        radius_match = abs(radius - polar_coords[i][0]) < 1e-2
        angle_match = abs(angle - polar_coords[i][1]) < 1e-2

        print(f"Original polar coordinates: (r = {polar_coords[i][0]:.2f}, θ = {polar_coords[i][1]:.2f} degrees)")
        print(f"Calculated polar coordinates: (r = {radius:.2f}, θ = {angle:.2f} degrees)")
        print(f"Cartesian coordinates: (x = {cartesian_coords[i][0]:.2f}, y = {cartesian_coords[i][1]:.2f})")
        print(f"Radius match: {radius_match}")
        print(f"Angle match: {angle_match}")
        print()

if __name__ == "__main__":
    main()