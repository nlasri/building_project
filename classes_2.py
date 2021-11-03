import numpy as np
from visualisation import *

class Building:
    def __init__(self, width, height, nbfloor):
        self.width = width
        self.height = height
        self.nbfloor = nbfloor
        self.areas = {}
        for i in range(nbfloor):
            self.areas[i]=[]

    def collision(self, new_area, floor):
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
        if area.coordinate_x + area.width > self.width:
            return True
        elif area.coordinate_y + area.height > self.height:
            return True
        return False

    def add_area(self, area, floor):
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
        if area in self.areas[floor]:
            self.areas[floor].remove(area)
        else:
            print("Error : the room doesn't exist")


class Area:
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
        for element in self.elements:
            if (new_element.coordinate_x + new_element.width > element.coordinate_x) and (new_element.coordinate_x < element.coordinate_x + element.width):
                if (new_element.coordinate_y + new_element.height > element.coordinate_y) and (new_element.coordinate_y < element.coordinate_y + element.height):
                    return True
                elif (new_element.coordinate_y < element.coordinate_y + element.height) and (new_element.coordinate_y + new_element.height > element.coordinate_y):
                    return True
            elif (new_element.coordinate_x < element.coordinate_x + element.width) and (new_element.coordinate_x + new_element.width > element.coordinate_x):
                if (new_element.coordinate_y + new_element.height > element.coordinate_y) and (new_element.coordinate_y < element.coordinate_y + element.height):
                    return True
                elif (new_element.coordinate_y < element.coordinate_y + element.height) and (new_element.coordinate_y + new_element.height > element.coordinate_y):
                    return True
        return False

    def area_not_in_building(self, element):
        if element.coordinate_x + element.width > self.width:
            return True
        elif element.coordinate_y + element.height > self.height:
            return True
        return False

    def add_element(self, element):
        if self.collision(element):

            print("Error : there is already an element at this place")
        elif self.area_not_in_building(element):
            print("Error : The element is not in the area")
        else :
            self.elements.append(element)

    def create_wall(self):
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
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coordinate_x(self):
        return self.coordinate_x

    def get_coordinate_y(self):
        return self.coordinate_y


class Wall(Element):
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)


class Door(Element):
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)

    def is_possible(self, area):
        table_walls = area.walls
        if self.coordinate_x == table_walls[0].coordinate_x:
            return(table_walls[1].coordinate_y < self.coordinate_y < table_walls[1].coordinate_y + table_walls[1].height)
        if self.coordinate_y == table_walls[0].coordinate_y:
            return(table_walls[0].coordinate_x < self.coordinate_x < table_walls[0].coordinate_x + table_walls[0].width)
        if self.coordinate_y == table_walls[2].coordinate_y:
            return(table_walls[2].coordinate_x < self.coordinate_x < table_walls[2].coordinate_x + table_walls[2].width)
        if self.coordinate_x == table_walls[3].coordinate_x:
            return(table_walls[3].coordinate_y < self.coordinate_y < table_walls[3].coordinate_y + table_walls[2].height)
        else:
            return(False)

class Room(Area):
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'red'
        self.name = 'room'

class Corridor(Area):
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'black'
        self.name = ''

class Outside(Area):
    def __init__(self, coordinate_x, coordinate_y, width, heigh):
        super().__init__(coordinate_x, coordinate_y, width, heigh)
        self.color = 'green'
        self.name = 'outside'






