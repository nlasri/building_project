# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""

import numpy as np
from visualisation import *

class Building:
    """This is the class of the building
    """
    def __init__(self, width, height, nbfloor):
        self.width = width
        self.height = height
        self.nbfloor = nbfloor
        self.areas = {}
        for i in range(nbfloor):
            self.areas[i]=[]

    def collision(self, new_area, floor):
        """This function returns True if the new area is on an existing area of a floor.

        Args:
            new_area (Area): New area
            floor (int): floor to check

        Returns:
            Boolean: True if the new area is on an existing area of a floor
        """
        for area in self.areas[floor]:
            if (new_area.coordinate_x + new_area.width > area.coordinate_x) and (new_area.coordinate_x < area.coordinate_x + area.width):
                if (new_area.coordinate_y + new_area.height > area.coordinate_y) and (new_area.coordinate_y < area.coordinate_y + area.height):
                    return True
                elif (new_area.coordinate_y < area.coordinate_y + area.height) and (new_area.coordinate_y + new_area.height > area.coordinate_y):
                    return True
            elif (new_area.coordinate_x < area.coordinate_x + area.width) and (new_area.coordinate_x + new_area.width > area.coordinate_x):
                if (new_area.coordinate_y + new_area.height > area.coordinate_y) and (new_area.coordinate_y < area.coordinate_y + area.height):
                    return True
                elif (new_area.coordinate_y < area.coordinate_y + area.height) and (new_area.coordinate_y + new_area.height > area.coordinate_y):
                    return True
        return False

    def area_not_in_building(self, area):
        """This function checks if the area in the building.

        Args:
            area (Area): Area

        Returns:
            boolean: True if the area is in the building.
        """
        if area.coordinate_x + area.width > self.width:
            return True
        elif area.coordinate_y + area.height > self.height:
            return True
        return False

    def add_area(self, area, floor):
        """This function add an area in a floor.

        Args:
            area (Area): area to add
            floor (int): Floor in which the area will be added
        """
        if self.collision(area, floor):
            print("Error : there is already an area at this place")
        elif self.area_not_in_building(area):
            print("Error : The area is not in the building")
        else :
            area.create_wall()
            self.areas[floor].append(area)

    def get_areas(self):
        return self.areas

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def delete_area(self, area, floor):
        """This function delete an area in a floor.

        Args:
            area (Area): area to delete
            floor (int): floor
        """
        if area in self.areas[floor]:
            self.areas[floor].remove(area)
        else:
            print("Error : the room doesn't exist")


class Area:
    """This is the class of the area.
    """
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.elements = []
        self.walls = []
        self.doors = []
        self.color = 'orange'
        self.name = 'area'

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coordinates(self):
        return np.array([self.coordinate_x, self.coordinate_y, self.width, self.height])

    def collision(self, new_element):
        """This function returns True if the new element is on an existing element.

        Args:
            new_element (Element): New element

        Returns:
            Boolean: True if the new element is on an existing element of a floor
        """
        for element in self.elements:
            if (new_element.coordinate_x + new_element.width > element.coordinate_x) and (new_element.coordinate_x < element.coordinate_x + element.width):
                if type(element)==Door:
                    return True
                elif (new_element.coordinate_y + new_element.height > element.coordinate_y) and (new_element.coordinate_y < element.coordinate_y + element.height):
                    return True
                elif (new_element.coordinate_y < element.coordinate_y + element.height) and (new_element.coordinate_y + new_element.height > element.coordinate_y):
                    return True
            elif (new_element.coordinate_x < element.coordinate_x + element.width) and (new_element.coordinate_x + new_element.width > element.coordinate_x):
                if type(element)==Door:
                    return True
                elif (new_element.coordinate_y + new_element.height > element.coordinate_y) and (new_element.coordinate_y < element.coordinate_y + element.height):
                    return True
                elif (new_element.coordinate_y < element.coordinate_y + element.height) and (new_element.coordinate_y + new_element.height > element.coordinate_y):
                    return True
        return False

    def element_not_in_area(self, element):
        """This function checks if the element in the area.

        Args:
            area (Element): element

        Returns:
            boolean: True if the element is in the area.
        """
        if element.coordinate_x + element.width > self.width:
            return True
        elif element.coordinate_y + element.height > self.height:
            return True
        return False

    def add_element(self, element):
        """This function add an element.

        Args:
            area (element): element to add
        """
        if self.collision(element):
            print("Error : there is already an element at this place")
        elif self.element_not_in_area(element):
            print("Error : The element is not in the area")
        else :
            self.elements.append(element)

    def create_wall(self):
        """This function creates the 4 walls of the area.
        """
        room_coordinates = self.get_coordinates()
        room_coordinates_abs = room_coordinates[0]
        room_coordinates_ord = room_coordinates[1]
        room_coordinates_width = room_coordinates[2]
        room_coordinates_height = room_coordinates[3]
        self.walls.append(Wall(room_coordinates_abs, room_coordinates_ord, room_coordinates_width, 0))
        self.walls.append(Wall(room_coordinates_abs, room_coordinates_ord, 0, room_coordinates_height))
        self.walls.append(Wall(room_coordinates_abs, room_coordinates_ord + room_coordinates_height, room_coordinates_width, 0))
        self.walls.append(Wall(room_coordinates_abs + room_coordinates_width, room_coordinates_ord, 0, room_coordinates_height))


    
class Element():
    """This is the class of an element.
    """
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.color = 'coral'
        self.name = 'element'

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coordinate_x(self):
        return self.coordinate_x

    def get_coordinate_y(self):
        return self.coordinate_y

    def get_coordinates(self):
        return np.array([self.coordinate_x, self.coordinate_y, self.width, self.height])


class Wall(Element):
    """This is the class of a wall
    """
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)


class Door(Element):
    """This is the class of a door.
    """
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'sienna'

    def is_possible(self, area):
        """This functions determines if it is possible to add a door in an area.

        Args:
            area (area): Area where the door will be added

        Returns:
            Boolean: True if the door can be added
        """
        if (self.height==0) and (self.coordinate_y==0):
            return True
        elif (self.height==0) and (self.coordinate_y==area.height):
            return True
        elif (self.width==0) and (self.coordinate_x==0):
            return True
        elif (self.width==0) and (self.coordinate_x==area.width):
            return True
        else:
            return(False)

class Room(Area):
    """This is the class of a Room.
    """
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'red'
        self.name = 'room'

class Corridor(Area):
    """This is the class of a corridor
    """
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'black'
        self.name = ''

class Outside(Area):
    """This is the class of an area outside
    """
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'green'
        self.name = 'outside'

