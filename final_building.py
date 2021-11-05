# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""

import pickle 
from classes import *
from builder import *
from cluster import *
import os

if os.path.getsize('building.obj') > 0:      
    with open('building.obj', "rb") as f:
        unpickler = pickle.Unpickler(f)
        building_import = unpickler.load()
else:
    print("empty")

print(building_import)


building_cluster = Building(10, 10, 3)
area_cluster = Room(0,0, 5, 5)
building_cluster.add_area(area_cluster, 1)
building_cluster.add_area(Area(5,0, 5,5), 1)
building_cluster.areas[1][0].add_element(Element(0,0, 2,2))

people_2 = []
for i in range(10): #10 is the number of persons in the area
    rand_abs = (5) * random.gauss(0,1) #5 is the width of the area
    rand_ord = 5* random.gauss(0,1) #5 is the height of the area
    people_2.append([rand_abs,rand_ord])

people = [[], people_2, []]


result = False
while not result:
    try:
        show_cluster(building_cluster ,people)
        result = True
    except:
         pass


