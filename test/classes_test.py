# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""

import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from classes import *

import unittest

#________________________TEST ADD AREAS IN BUILDING_____________________________
class testbuilding(unittest.TestCase):
    def width_test(self):
        building_test = Building(30, 20, 2)
        self.assertEqual(building_test.width, 30)
    def height_test(self):
        building_test = Building(30, 20, 2)
        self.assertEqual(building_test.height, 20)
    def floors_test(self):
        building_test = Building(30, 20, 2)
        self.assertEqual(building_test.nbfloor, 2)
    def floors_test(self):
        building_test = Building(30, 20, 2)
        self.assertEqual(building_test.areas, None)

class testarea(unittest.TestCase):
    def width_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.width, 5)
    def height_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.height, 10)
    def coordinatex_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.coordinate_x, 1)
    def coordinatey_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.coordinate_y, 2)
    def elements_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.elements, None)
    def doors_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.walls, None)
    def walls_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.doors, None)
    def color_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.color, 'orange')
    def name_test(self):
        area_test = Area(1, 2, 5, 10)
        self.assertEqual(area_test.name, 'area')

class addWrongAreaTest(unittest.TestCase):
    def test_add_area1(self): #the existing area of the building is inside the new area
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(9,9, 19, 19)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1

    def test_add_area2(self): #the new area is on the left bottom corner
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(0,0, 11, 11)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1

    def test_add_area3(self): #the new area is on the right bottom corner
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(14,14, 11, 11)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 1) #There is 1 area in the building floor 1

    def test_add_area_outside_building(self): #the new area is outside the building
        building_test = Building(20, 20, 2)
        
        area1 = Area(19,19, 5, 5)
        building_test.add_area(area1, 1)

        self.assertEqual(len(building_test.areas[1]), 0) #There is no area in the building floor 1


class addGoodAreaTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        area2 = Area(0,0, 5, 5)
        building_test.add_area(area2, 1)

        self.assertEqual(len(building_test.areas[1]), 2) #There is 2 areas in the building floor 1

class deleteAreaTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        building_test.delete_area(area1, 1)

        self.assertEqual(len(building_test.areas[1]), 0) #There is no area in the building floor 1

class addRoomTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        room = Room(0,0, 5, 5)
        building_test.add_area(room, 1)

        self.assertEqual(len(building_test.areas[1]), 2) #There is 2 areas in the building floor 1

class addCorridorTest(unittest.TestCase):
    def test_add_area(self): 
        building_test = Building(20, 20, 2)
        
        area1 = Area(10,10, 5, 5)
        building_test.add_area(area1, 1)

        corridor = Corridor(0,0, 5, 5)
        building_test.add_area(corridor, 1)

        self.assertEqual(len(building_test.areas[1]), 2)


#________________________TEST ADD ELEMENTS IN AREA_____________________________

class testelement(unittest.TestCase):
    def width_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.width, 5)
    def height_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.height, 10)
    def coordinatex_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.coordinate_x, 1)
    def coordinatey_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.coordinate_y, 2)
    def color_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.color, 'coral')
    def name_test(self):
        element_test = Element(1, 2, 5, 10)
        self.assertEqual(element_test.name, 'element')

class addWrongElementTest(unittest.TestCase):
    def test_add_element1(self): #the existing element of the area is inside the new element
        area_test = Area(0, 0, 10, 10)
        
        element1 = Element(1,1, 5, 5)
        area_test.add_element(element1)

        element2 = Area(0,0, 9, 9)
        area_test.add_element(element2)

        self.assertEqual(len(area_test.elements), 1) #There is 1 area in the building floor 1

    def test_add_element2(self): #the new element is ont the left corner of the existing one
        area_test = Area(0, 0, 10, 10)
        
        element1 = Element(5,5, 5, 5)
        area_test.add_element(element1)

        element2 = Area(1,1, 5, 5)
        area_test.add_element(element2)

        self.assertEqual(len(area_test.elements), 1) #There is 1 area in the building floor 1

    def test_add_element_outside_area(self): #the new area is outside the building
        area_test = Area(0, 0, 10, 10)
        
        element1 = Element(9,9, 5, 5)
        area_test.add_element(element1)

        self.assertEqual(len(area_test.elements), 0) #There is no element in the area

class createwallsTest(unittest.TestCase):
    def test_wall0(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        wall0=Wall(0,0,10,0)
        self.assertTrue((area_test.walls[0].get_coordinates() == wall0).all)

    def test_wall0(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        wall1=Wall(0,0,0,10)
        self.assertTrue((area_test.walls[1].get_coordinates() == wall1).all)

    def test_wall0(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        wall2=Wall(0,10,10,0)
        self.assertTrue((area_test.walls[2].get_coordinates() == wall2).all)

    def test_wall0(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        wall3=Wall(10,0,0,10)
        self.assertTrue((area_test.walls[3].get_coordinates() == wall3).all)

class doorTest(unittest.TestCase):
    def test_door(self): 
        door_test = Door(0, 0, 2, 0)
        self.assertEqual(door_test.color, 'sienna')

    def test_place_door_wrong(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        door_test = Door(1, 0, 0, 2)
        self.assertFalse(door_test.is_possible(area_test))

    def test_place_door_good(self): 
        area_test = Area(0, 0, 10, 10)
        area_test.create_wall()
        door_test = Door(1, 0, 2, 0)
        self.assertTrue(door_test.is_possible(area_test))


if __name__ == '__main__':
    unittest.main()
