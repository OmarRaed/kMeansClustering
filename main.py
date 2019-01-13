import random
import math
import numpy as np
import matplotlib.pyplot as plt


# A Function to initialize random points and centroids
def initialize_random_points(min_x, max_x, min_y, max_y, length):
    rand_points = []
    for n in range(0, length):
        x = random.randrange(min_x, max_x)
        y = random.randrange(min_y, max_y)
        rand_points.append([x, y])
    return rand_points


# A Function that calculate the distance matrix
def calculate_distance_matrix(points, centroids):
    distance_matrix = []
    for n in range(0, len(points)):
        distance = []
        for m in range(0, len(centroids)):
            d = math.sqrt((points[n][0] - centroids[m][0]) ** 2
                          + (points[n][1] - centroids[m][1]) ** 2)
            distance.append(d)
        distance_matrix.append(distance)
    return distance_matrix


# A Function that calculate the group matrix
def calculate_group_matrix(distance_matrix, clusters_num):
    g = []
    for n in range(0, len(distance_matrix)):
        min_index = np.argmin(distance_matrix[n])
        point_group = [0] * clusters_num
        point_group[min_index] = 1
        g.append(point_group)
    return g


# A Function that calculate the center for an individual centroid
def calculate_new_centroids(original_points, distance_matrix, group_index):
    g = []
    for n in range(0, len(distance_matrix)):
        min_index = np.argmin(distance_matrix[n])
        if min_index == group_index:
            g.append(original_points[n])
    g_sum = [sum(x) for x in zip(*g)]
    g = [x / len(g) for x in g_sum]
    return g


# A Function that calculate and update the new centroids
def update_new_centers(points, distance_matrix, centroids):
    new_centroids = []
    for x in range(0, len(centroids)):
        current_centroid = calculate_new_centroids(points, distance_matrix, x)
        if len(current_centroid) == 0:
            new_centroids.append(centroids[x])
        else:
            new_centroids.append(current_centroid)
    return new_centroids


# A Function that plot the points along with the centroids
def plot_points(points, clusters_centers, fig_num):
    fig = plt.figure()
    x = [row[0] for row in points]
    y = [row[1] for row in points]
    plt.plot(x, y, 'ro')
    x = [row[0] for row in clusters_centers]
    y = [row[1] for row in clusters_centers]
    plt.plot(x, y, 'bo')
    plt.axis([0, 50, 0, 50])
    plt.show()
    fig.savefig("figure" + str(fig_num), facecolor='w', edgecolor='w',
                orientation='portrait', pad_inches=0.1)


POINTS_NUM = 25
CENTROIDS_NUM = 4
X_MIN = 0
X_MAX = 50
Y_MIN = 0
Y_MAX = 50

# Initialize the random points
randPoints = initialize_random_points(X_MIN, X_MAX, Y_MIN, Y_MAX, POINTS_NUM)

# Initialize random centroids
centroids = initialize_random_points(X_MIN, X_MAX, Y_MIN, Y_MAX, CENTROIDS_NUM)

# Initialize iterations number variable
iterations = 0

# plot the points along with the initialized centroids
plot_points(randPoints, centroids, iterations)

# print the points
print(randPoints)

# A boolean to determine if the group matrices converged or not
converge = False

while not converge:

    # print the centroids
    print(centroids)

    # calculate the distance matrix and print it
    DistanceMatrix = calculate_distance_matrix(randPoints, centroids)
    print(DistanceMatrix)

    # calculate the group matrix and print it
    GroupMatrix = calculate_group_matrix(DistanceMatrix, len(centroids))
    print(GroupMatrix)

    # calculate the new centroids and print it
    newCentroids = update_new_centers(randPoints, DistanceMatrix, centroids)
    print(newCentroids)

    # plot the new centroids
    plot_points(randPoints, newCentroids, iterations + 1)

    # calculate the new distance matrix
    newDistanceMatrix = calculate_distance_matrix(randPoints, newCentroids)
    print(newDistanceMatrix)

    # calculate the new group matrix
    newGroupMatrix = calculate_group_matrix(newDistanceMatrix, len(newCentroids))
    print(newGroupMatrix)

    # if group matrices matched -> Converge achieved
    if GroupMatrix == newGroupMatrix:
        print("Converge achieved")
        converge = True
    else:
        print("Converge not achieved")
        centroids = newCentroids

    # increment iterations by one
    iterations = iterations + 1

print(centroids)
print("Iterations Number " + str(iterations))
