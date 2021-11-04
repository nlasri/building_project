# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:29:28 2021

@author: Alain
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:29:28 2021

@author: Alain
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def Kmeans(X_train,X_test):
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X_train)
    pred = kmeans.predict(X_test)
    return(pred)


# def pile_vide(): return []
# def empiler(S, A): S.append(A)
# def depiler(S): S.pop()

# def sommet(S): return S[-1]
# def sous_sommet(S): return S[-2]

# def determinant(u, v):
#     return u[0] * v[1] - u[1] * v[0]

# def vecteur(A, B):
#     return (B[0] - A[0], B[1] - A[1])

# def graham2(A):
#     S = pile_vide()
#     Omega = min_lexico(A)
#     trier_angles_distances(Omega, A)
#     A1 = supprimer_alignes(A, Omega)
#     empiler(S, A1[0])
#     empiler(S, A1[1])
#     empiler(S, A1[2])
#     for i in range(3, len(A1)):
#         while pseudo_angle(sous_sommet(S), sommet(S), A1[i]) <= 0:
#             depiler(S)
#             #print(S)
#             empiler(S, A1[i])
#     return S


# A Python3 program to find convex hull of a set of points. Refer
# https://www.geeksforgeeks.org/orientation-3-ordered-points/
# for explanation of orientation()
 
# from functools import cmp_to_key
 
# # A class used to store the x and y coordinates of points
# class Point:
#     def __init__(self, x = None, y = None):
#         self.x = x
#         self.y = y
 
# # A global point needed for sorting points with reference
# # to the first point
# p0 = Point(0, 0)
 
# # A utility function to find next to top in a stack
# def nextToTop(S):
#     return S[-2]
 
# # A utility function to return square of distance
# # between p1 and p2
# def distSq(p1, p2):
#     return ((p1.x - p2.x) * (p1.x - p2.x) +
#             (p1.y - p2.y) * (p1.y - p2.y))
 
# # To find orientation of ordered triplet (p, q, r).
# # The function returns following values
# # 0 --> p, q and r are collinear
# # 1 --> Clockwise
# # 2 --> Counterclockwise
# def orientation(p, q, r):
#     val = ((q.y - p.y) * (r.x - q.x) -
#            (q.x - p.x) * (r.y - q.y))
#     if val == 0:
#         return 0  # collinear
#     elif val > 0:
#         return 1  # clock wise
#     else:
#         return 2  # counterclock wise
 
# # A function used by cmp_to_key function to sort an array of
# # points with respect to the first point
# def compare(p1, p2):
   
#     # Find orientation
#     o = orientation(p0, p1, p2)
#     if o == 0:
#         if distSq(p0, p2) >= distSq(p0, p1):
#             return -1
#         else:
#             return 1
#     else:
#         if o == 2:
#             return -1
#         else:
#             return 1
 
# # Prints convex hull of a set of n points.
# def convexHull(points, n):
   
#     # Find the bottommost point
#     ymin = points[0].y
#     min = 0
#     for i in range(1, n):
#         y = points[i].y
 
#         # Pick the bottom-most or chose the left
#         # most point in case of tie
#         if ((y < ymin) or
#             (ymin == y and points[i].x < points[min].x)):
#             ymin = points[i].y
#             min = i
 
#     # Place the bottom-most point at first position
#     points[0], points[min] = points[min], points[0]
 
#     # Sort n-1 points with respect to the first point.
#     # A point p1 comes before p2 in sorted output if p2
#     # has larger polar angle (in counterclockwise
#     # direction) than p1
#     p0 = points[0]
#     points = sorted(points, key=cmp_to_key(compare))
 
#     # If two or more points make same angle with p0,
#     # Remove all but the one that is farthest from p0
#     # Remember that, in above sorting, our criteria was
#     # to keep the farthest point at the end when more than
#     # one points have same angle.
#     m = 1  # Initialize size of modified array
#     for i in range(1, n):
       
#         # Keep removing i while angle of i and i+1 is same
#         # with respect to p0
#         while ((i < n - 1) and
#         (orientation(p0, points[i], points[i + 1]) == 0)):
#             i += 1
 
#         points[m] = points[i]
#         m += 1  # Update size of modified array
 
#     # If modified array of points has less than 3 points,
#     # convex hull is not possible
#     if m < 3:
#         return
 
#     # Create an empty stack and push first three points
#     # to it.
#     S = []
#     S.append(points[0])
#     S.append(points[1])
#     S.append(points[2])
 
#     # Process remaining n-3 points
#     for i in range(3, m):
       
#         # Keep removing top while the angle formed by
#         # points next-to-top, top, and points[i] makes
#         # a non-left turn
#         while ((len(S) > 1) and
#         (orientation(nextToTop(S), S[-1], points[i]) != 2)):
#             S.pop()
#         S.append(points[i])
 
#     # Now stack has the output points,
#     # print contents of stack
#     while S:
#         p = S[-1]
#         print("(" + str(p.x) + ", " + str(p.y) + ")")
#         S.pop()
 
# # Driver Code
# input_points = [(0, 3), (1, 1), (2, 2), (4, 4),
#                 (0, 0), (1, 2), (3, 1), (3, 3)]
# points = []
# for point in input_points:
#     points.append(Point(point[0], point[1]))
# n = len(points)
# convexHull(points, n)





# A Python3 program to find convex hull of a set of points. Refer
# https://www.geeksforgeeks.org/orientation-3-ordered-points/
# for explanation of orientation()
 
from functools import cmp_to_key
 
# A class used to store the x and y coordinates of points
class Point:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
 
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
 
    # Now stack has the output points,
    # print contents of stack
    # while S:
    #     p = S[-1]
    #     #print("(" + str(p[0]) + ", " + str(p[1]) + ")")
    #     print(p)
    #     S.pop()

    return(S)
 
# Driver Code
input_points = [[0, 3], [1, 1], [2, 2], [4, 4],
                [0, 0], [1, 2], [3, 1], [3, 3]]
# points = []
# for point in input_points:
#     points.append(Point(point[0], point[1]))
n = len(input_points)
final_list = convexHull(input_points, n)


# fig, ax = plt.subplots()
# ax.scatter()
