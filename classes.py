# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:26:36 2021

@author: sguerrag
"""

class Building:
    
    def __init__(self, name_building, nb_floors_max):
        self.name_building = name_building
        self.nb_floors_max = nb_floors_max
        
        
class Element:
    
    
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
class Wall(Element):
    thickness = 0
    def __init__(self,color):
        self.color = color
    
class Area:
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name
        
class Room(Area):
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name
        
class Outside(Area):
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name
        
class Corridor(Area):
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name    
    
B = Building("B",10)