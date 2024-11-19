import math
import random

def main():
    n = int(input("Enter the number of points: "))

    spherical_coords = [[0] * 3 for _ in range(n)] 
    cartesian_coords = [[0] * 3 for _ in range(n)] 

    for i in range(n):
        radius = random.random() * 10  
        theta_in_degrees = random.random() * 360  
        phi_in_degrees = random.random() * 180  

        theta_in_radians = math.radians(theta_in_degrees)
        phi_in_radians = math.radians(phi_in_degrees)

        x = radius * math.sin(phi_in_radians) * math.cos(theta_in_radians)
        y = radius * math.sin(phi_in_radians) * math.sin(theta_in_radians)
        z = radius * math.cos(phi_in_radians)

        spherical_coords[i][0] = radius
        spherical_coords[i][1] = theta_in_degrees
        spherical_coords[i][2] = phi_in_degrees
        cartesian_coords[i][0] = x
        cartesian_coords[i][1] = y
        cartesian_coords[i][2] = z

    for i in range(n):
        radius = math.sqrt(cartesian_coords[i][0] ** 2 + cartesian_coords[i][1] ** 2 + cartesian_coords[i][2] ** 2)

        theta = math.degrees(math.atan2(cartesian_coords[i][1], cartesian_coords[i][0]))

        if cartesian_coords[i][0] < 0:
            theta += 180
        elif cartesian_coords[i][0] == 0 and cartesian_coords[i][1] < 0:
            theta -= 180

        phi = math.degrees(math.acos(cartesian_coords[i][2] / radius))

        if theta < 0:
            theta += 360

        radius_match = abs(radius - spherical_coords[i][0]) < 1e-2
        theta_match = abs(theta - spherical_coords[i][1]) < 1e-2
        phi_match = abs(phi - spherical_coords[i][2]) < 1e-2

        print(f"Original spherical coordinates: (r = {spherical_coords[i][0]:.2f}, θ = {spherical_coords[i][1]:.2f} degrees, φ = {spherical_coords[i][2]:.2f} degrees)")
        print(f"Calculated spherical coordinates: (r = {radius:.2f}, θ = {theta:.2f} degrees, φ = {phi:.2f} degrees)")
        print(f"Cartesian coordinates: (x = {cartesian_coords[i][0]:.2f}, y = {cartesian_coords[i][1]:.2f}, z = {cartesian_coords[i][2]:.2f})")
        print(f"Radius match: {radius_match}")
        print(f"Theta match: {theta_match}")
        print(f"Phi match: {phi_match}")
        print()

if __name__ == "__main__":
    main()