import math
import random

def main():
    n = int(input("Enter the number of points: "))

    cartesian_coords = [[0] * 3 for _ in range(n)]  
    spherical_coords = [[0] * 3 for _ in range(n)]  

    for i in range(n):
        x = random.random() * 20 - 10  
        y = random.random() * 20 - 10  
        z = random.random() * 20 - 10  

        radius = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan2(y, x) 
        phi = math.acos(z / radius)  

        cartesian_coords[i][0] = x
        cartesian_coords[i][1] = y
        cartesian_coords[i][2] = z
        spherical_coords[i][0] = radius
        spherical_coords[i][1] = theta
        spherical_coords[i][2] = phi

    for i in range(n):
        j = (i + 1) % n  

        distance_3d = math.sqrt(
            (cartesian_coords[j][0] - cartesian_coords[i][0]) ** 2 +
            (cartesian_coords[j][1] - cartesian_coords[i][1]) ** 2 +
            (cartesian_coords[j][2] - cartesian_coords[i][2]) ** 2
        )

        x1, y1 = cartesian_coords[i][0], cartesian_coords[i][1]
        x2, y2 = cartesian_coords[j][0], cartesian_coords[j][1]
        radius1 = math.sqrt(x1 ** 2 + y1 ** 2)
        radius2 = math.sqrt(x2 ** 2 + y2 ** 2)
        angle1 = math.atan2(y1, x1)
        angle2 = math.atan2(y2, x2)
        distance_polar = math.sqrt(
            (radius2 * math.cos(angle2) - radius1 * math.cos(angle1)) ** 2 +
            (radius2 * math.sin(angle2) - radius1 * math.sin(angle1)) ** 2
        )

        r1, theta1, phi1 = spherical_coords[i]
        r2, theta2, phi2 = spherical_coords[j]
        distance_3d_sphere = math.sqrt(
            r1 ** 2 + r2 ** 2 -
            2 * r1 * r2 * (math.sin(phi1) * math.sin(phi2) * math.cos(theta2 - theta1) +
                           math.cos(phi1) * math.cos(phi2))
        )

        radius_sphere = 10
        surface_distance = radius_sphere * math.acos(
            math.sin(phi1) * math.sin(phi2) * math.cos(theta2 - theta1) +
            math.cos(phi1) * math.cos(phi2)
        )

        print(f"Point 1: (x = {cartesian_coords[i][0]:.2f}, y = {cartesian_coords[i][1]:.2f}, z = {cartesian_coords[i][2]:.2f})")
        print(f"Point 2: (x = {cartesian_coords[j][0]:.2f}, y = {cartesian_coords[j][1]:.2f}, z = {cartesian_coords[j][2]:.2f})")
        print(f"Distance in Cartesian coordinates: {distance_3d:.2f}")
        print(f"Distance in Polar coordinates: {distance_polar:.2f}")
        print(f"Distance in spherical coordinates (volume): {distance_3d_sphere:.2f}")
        print(f"Distance in spherical coordinates (surface): {surface_distance:.2f}")
        print()

if __name__ == "__main__":
    main()