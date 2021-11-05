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


print(building_import.areas)

building_alain = Building(10, 10, 3)
area_alain = Room(0,0, 5, 5)
building_alain.add_area(area_alain, 1)
building_alain.add_area(Area(5,0, 5,5), 1)
building_alain.areas[1][0].add_element(Element(0,0, 2,2))

people_1 = [[0,3],[2,2], [1,2], [3,4], [1,1], [3,2]]
people_2 = []
for i in range(20):
    rand_abs = (5) * random.gauss(0,1)
    rand_ord = 5* random.gauss(0,1)
    people_2.append([rand_abs,rand_ord])
people = [[], people_2, []]


show_cluster(building_import,people)