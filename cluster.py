# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import random
from functools import cmp_to_key

def Kmeans_people(X_train,X_test,k):
    """Return the prediction according to the KMeans method
    Args : X_train (np.array) : training set
           X_test (np.array) : test set
           k (int) : number of clusters
    Returns : pred (np.array) : the predictions of the label of X_test"""
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X_train)
    pred = kmeans.predict(X_test)
    return(pred)

def create_X_train_floor(area):
    """Create Training Set of a floor by separating the different areas
    Args : area (list[Area]) : list of areas of the floor
    Returns : people_coordinates (np.array) table of the coordinates of people created"""
    people_coordinate = np.zeros((0,2))
    nb_areas = len(area)
    for j in range(nb_areas):
        people_area = np.zeros((20,2))
        coordinates = area[j].get_coordinates()
        absc = coordinates[0]
        ordi = coordinates[1]
        length = coordinates[2]
        height = coordinates[3]
        for i in range(20):
            rand_abs = ((length + absc) - absc) * random.gauss(0,1) + absc
            rand_ord = ((height + ordi) - ordi) * random.gauss(0,1) + ordi
            people_area[i][0] = rand_abs
            people_area[i][1] = rand_ord
        people_coordinate = np.concatenate((people_coordinate,people_area))
    return(people_coordinate)

            

 

 
# A global point needed for sorting points with reference
# to the first point
p0 = [0,0]
 
# A utility function to find next to top in a stack
def nextToTop(S):
    return S[-2]
 
# A utility function to return square of distance
# between p1 and p2
def distSq(p1, p2):
    return (((p1[0] - p2[0])**2) +
            ((p1[1] - p2[1]))**2)
 
# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0]) -
           (q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clock wise
    else:
        return 2  # counterclock wise
 
# A function used by cmp_to_key function to sort an array of
# points with respect to the first point
def compare(p1, p2):
   
    # Find orientation
    o = orientation(p0, p1, p2)
    if o == 0:
        if distSq(p0, p2) >= distSq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1
 
# Prints convex hull of a set of n points.
def convexHull(points, n):
    """Return the points that compose the Graham convex envelope
    Args : points (list) : list of points
           n : length of points
    Returns : S (list) : list of points that compose the Graham convex envelope"""
   
    # Find the bottommost point
    ymin = points[0][1]
    mini = 0
    for i in range(1, n):
        y = points[i][1]
 
        # Pick the bottom-most or chose the left
        # most point in case of tie
        if ((y < ymin) or
            (ymin == y and points[i][0] < points[mini][0])):
            ymin = points[i][1]
            mini = i
 
    # Place the bottom-most point at first position
    points[0], points[mini] = points[mini], points[0]
 
    # Sort n-1 points with respect to the first point.
    # A point p1 comes before p2 in sorted output if p2
    # has larger polar angle (in counterclockwise
    # direction) than p1
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))
 
    # If two or more points make same angle with p0,
    # Remove all but the one that is farthest from p0
    # Remember that, in above sorting, our criteria was
    # to keep the farthest point at the end when more than
    # one points have same angle.
    m = 1  # Initialize size of modified array
    for i in range(1, n):
       
        # Keep removing i while angle of i and i+1 is same
        # with respect to p0
        while ((i < n - 1) and
        (orientation(p0, points[i], points[i + 1]) == 0)):
            i += 1
 
        points[m] = points[i]
        m += 1  # Update size of modified array
 
    # If modified array of points has less than 3 points,
    # convex hull is not possible
    if m < 3:
        return
 
    # Create an empty stack and push first three points
    # to it.
    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])
 
    # Process remaining n-3 points
    for i in range(3, m):
       
        # Keep removing top while the angle formed by
        # points next-to-top, top, and points[i] makes
        # a non-left turn
        while ((len(S) > 1) and
        (orientation(nextToTop(S), S[-1], points[i]) != 2)):
            S.pop()
        S.append(points[i])
    return(S)


def trace_graham(input_points,final_list, fig, ax):
    """Plot the Graham convex envelope
    Args : input_points (list) : list of points
           final_list (list) : list of points tha compose the Graham convex envelope
           fig (fig) : figure to plot
           ax (ax) : ax to plot"""
    x_points = [P[0] for P in input_points]
    y_points = [P[1] for P in input_points]
    ax.plot(x_points, y_points, 'ok', markersize=1)
    xs = [P[0] for P in final_list]
    ys = [P[1] for P in final_list]
    xs.append(final_list[0][0])
    ys.append(final_list[0][1])
    ax.plot(xs, ys, 'k')
    ax.plot(xs, ys, 'ro', markersize=6)
    ax.grid()


def repartir_clusters(points,pred, k):
    """Put the points in a list according to their label
    Args : points (list) : list of points
           pred (list) : list of labels
           k (int) : list of clusters
    Returns : list_clusters : list of points according to their clusters"""
    n = len(points)
    list_cluster = []
    for i in range(k):
        list_cluster.append([])
    for i in range(n):
        list_cluster[pred[i]].append(points[i])
    return(list_cluster)
            

def show_cluster(building,people):
    """Plot the Graham convex envelop per floor according to the clusters
    Args : building (Building) : building object
           people (list) : list of people's coordinates"""
    n = len(building.areas)
    for i in range(n):
        if people[i] != []:
            Xtrain_floor_i = create_X_train_floor(building.areas[i])
        k = len(building.areas[i])
        fig, ax = plt.subplots()
        plt.title("Floor " + str(i))
        ax.grid()
        if k > 0 and people[i] != []:
            pred_i = Kmeans_people(Xtrain_floor_i,people[i],k)
            list_cluster = repartir_clusters(people[i], pred_i, k)
            for j in range(k):
                list_graham = convexHull(list_cluster[j], len(list_cluster[j]))
                trace_graham(people[i], list_graham, fig, ax)
    plt.show()