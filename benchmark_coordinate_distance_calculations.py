import math
import random
import time

def main():
    num_points = 1000 

    cartesian_coords = [[random.random() * 20 - 10 for _ in range(3)] for _ in range(num_points)]

    start_time = time.time()
    distances_cartesian = [[0] * num_points for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                distances_cartesian[i][j] = math.sqrt(
                    (cartesian_coords[j][0] - cartesian_coords[i][0]) ** 2 +
                    (cartesian_coords[j][1] - cartesian_coords[i][1]) ** 2 +
                    (cartesian_coords[j][2] - cartesian_coords[i][2]) ** 2
                )
    
    print(f"Time for Cartesian coordinates: {int((time.time() - start_time) * 1000)} ms")

    polar_coords = [[0] * 2 for _ in range(num_points)]
    
    for i in range(num_points):
        radius = math.sqrt(cartesian_coords[i][0] ** 2 + cartesian_coords[i][1] ** 2)
        angle = math.atan2(cartesian_coords[i][1], cartesian_coords[i][0]) * (180 / math.pi)
        polar_coords[i][0] = radius
        polar_coords[i][1] = angle

    start_time = time.time()
    distances_polar = [[0] * num_points for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                radius1, radius2 = polar_coords[i][0], polar_coords[j][0]
                angle1, angle2 = polar_coords[i][1] * (math.pi / 180), polar_coords[j][1] * (math.pi / 180)
                distances_polar[i][j] = math.sqrt(
                    (radius2 * math.cos(angle2) - radius1 * math.cos(angle1)) ** 2 +
                    (radius2 * math.sin(angle2) - radius1 * math.sin(angle1)) ** 2
                )
    
    print(f"Time for Polar coordinates: {int((time.time() - start_time) * 1000)} ms")

    spherical_coords = [[0] * 3 for _ in range(num_points)]

    for i in range(num_points):
        radius = math.sqrt(cartesian_coords[i][0] ** 2 + cartesian_coords[i][1] ** 2 + cartesian_coords[i][2] ** 2)
        theta = math.atan2(cartesian_coords[i][1], cartesian_coords[i][0])
        phi = math.acos(cartesian_coords[i][2] / radius)
        spherical_coords[i][0] = radius
        spherical_coords[i][1] = theta
        spherical_coords[i][2] = phi

    start_time = time.time()
    distances_volume = [[0] * num_points for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                r1, theta1, phi1 = spherical_coords[i]
                r2, theta2, phi2 = spherical_coords[j]
                distances_volume[i][j] = math.sqrt(
                    r1 ** 2 + r2 ** 2 - 
                    2 * r1 * r2 * (math.sin(phi1) * math.sin(phi2) * math.cos(theta2 - theta1) +
                                   math.cos(phi1) * math.cos(phi2))
                )
    
    print(f"Time for volume distance calculation: {int((time.time() - start_time) * 1000)} ms")

    start_time = time.time()
    distances_surface = [[0] * num_points for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                r1, theta1, phi1 = spherical_coords[i]
                r2, theta2, phi2 = spherical_coords[j]
                distances_surface[i][j] = r1 * math.acos(
                    math.sin(phi1) * math.sin(phi2) * math.cos(theta2 - theta1) +
                    math.cos(phi1) * math.cos(phi2)
                )
    
    print(f"Time for surface distance calculation: {int((time.time() - start_time) * 1000)} ms")

if __name__ == "__main__":
    main()