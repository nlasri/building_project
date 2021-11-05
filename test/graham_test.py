# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:40:33 2021

@author: Alain
"""
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from cluster import *
import unittest


#_______________________________Test Graham Convex Envelop Points_____________________________
class CheckGrahamPoint(unittest.TestCase):
    def test_points(self):
        input_points = [[0, 3], [1, 1], [2, 2], [4, 4],[0, 0], [1, 2], [3, 1], [3, 3]]
        n = len(input_points)
        envelop_points = convexHull(input_points,n)
        self.assertEqual(envelop_points, [[0,0], [3,1], [4,4], [0,3]])

if __name__ == "__main__":
    unittest.main()