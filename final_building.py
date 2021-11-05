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


people_2 = []
for i in range(10):
    rand_abs = (5) * random.gauss(0,1)
    rand_ord = 5* random.gauss(0,1)
    people_2.append([rand_abs,rand_ord])

people_1 = []
for i in range(10):
    rand_abs = (5) * random.gauss(0,1)
    rand_ord = 5* random.gauss(0,1)
    people_1.append([rand_abs,rand_ord])
people = [people_1, people_2, []]


show_cluster(building_import ,people)