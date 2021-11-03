import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from classes_2 import *

import unittest


class addWrongAreaTest(unittest.TestCase):
    def test_add_area(self): #the existing area of the building would be inside the new area
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(9,9, 19, 19)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1

    def test_add_area(self): #the new area is on the left bottom corner
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(0,0, 11, 11)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1

    def test_add_area(self): #the new area is on the right bottom corner
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(14,14, 11, 11)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1


class addGoodAreaTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(0,0, 5, 5)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 2) #There is 2 areas in the building floor 1

class addRoomTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        room = Room(0,0, 5, 5)
        building_test.add_area(room, 1)

        self.assertEqual(len(building_test.areas[1]), 2) #There is 2 areas in the building floor 1

if __name__ == '__main__':
    unittest.main()
