# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:26:36 2021

@author: sguerrag
"""

import numpy as np

class Building:
    
    def __init__(self,nb_rooms_max,floor = 1, name_building = "", nb_floors_max = 5,areas =  "",elements = ""):
        self.name_building = name_building
        self.nb_floors_max = nb_floors_max
        self.area = areas
        self.element = elements
        self.floor = floor
        self.nb_rooms_max_longueur = 6
        self.nb_rooms_max_largeur = 6
        self.nb_rooms_max = 36
        self.grid_lenght = 12
        self.grid_height = 12
        self.space = np.zeros((self.nb_floors_max,self.nb_rooms_max_longueur,self.nb_rooms_max_largeur,4))
        self.space_element = np.zeros((self.nb_floors_max,self.grid_lenght,self.grid_height,4))
        
    def get_place_areas(self,number):
        return(number)
    
    def get_space(self):
        return(self.space)

    def change_arrangement(self,arrangement,floor):
        self.space[floor] = arrangement

    def get_space_element(self):
        return(self.space_element)

    def change_arrangement_element(self,arrangement,floor):
        self.space_element[floor] = arrangement
        
class Element:
    
    
    def __init__(self, coordinates,floor,l1,l2):
        self.coordinates = coordinates
        self.floor = floor
        self.nb_rooms_max = 40
        self.place = Building(self.floor, self.nb_rooms_max)
        self.nb_rooms_max_longueur = 6
        self.nb_rooms_max_largeur = 6
        self.longueur_one_room = l1
        self.largeur_one_room = l2
    
        
    def set_place_building(self):
        element_coordinates = self.place.get_space_element()[self.floor]
        print(element_coordinates[self.coordinates[0]][self.coordinates[1]])
        if np.all((element_coordinates[self.coordinates[0]][self.coordinates[1]]) == [0,0,0,0]): #np.all pour que toutes les valeurs doivent être égales.
            element_coordinates[self.coordinates[0]][self.coordinates[1]] = self.coordinates
            print("Set the element ok")
        else:
            print("Space occupied")
        return(element_coordinates)

    def set_many_places_building(self,element_many_coordinates):
        n = len(element_many_coordinates)
        element_coordinates = self.place.get_space()[self.floor]
        for i in range(n):
            element_coordinates = self.set_place_building(element_many_coordinates[i])
        return(element_coordinates)

    def put_arrangement_element_building(self,arrangement):
        #place_building = self.place.get_space()
        #place_building[self.floor] = arrangement
        return(arrangement)
                
        
        
class Wall(Element):

    def __init__(self, room):
        # self.coordinates = coordinates
        # self.floor = floor
        # self.nb_rooms_max = 40
        # self.place = Building(self.floor, self.nb_rooms_max)
        # self.nb_rooms_max_longueur = 6
        # self.nb_rooms_max_largeur = 6
        # self.longueur_one_room = l1
        # self.largeur_one_room = l2
        self.room = room

    def create_wall(self):
        room_coordinates = self.room.get_coordinates()
        table_walls = np.zeros((4,4))
        room_coordinates_abs = room_coordinates[0]
        room_coordinates_ord = room_coordinates[1]
        room_coordinates_length = room_coordinates[2]
        room_coordinates_height = room_coordinates[3]
        table_walls[0] = [room_coordinates_abs, room_coordinates_ord, room_coordinates_length, 0]
        table_walls[1] = [room_coordinates_abs, room_coordinates_ord, 0, room_coordinates_height]
        table_walls[2] = [room_coordinates_abs, room_coordinates_ord + room_coordinates_height, room_coordinates_length, 0]
        table_walls[3] = [room_coordinates_abs + room_coordinates_length, room_coordinates_ord, 0, room_coordinates_height]
        return(table_walls)

class Door(Element):

    def __init__(self, coordinates,floor,l1,l2,walls):
        self.coordinates = coordinates
        self.floor = floor
        self.nb_rooms_max = 40
        self.place = Building(self.floor, self.nb_rooms_max)
        self.nb_rooms_max_longueur = 6
        self.nb_rooms_max_largeur = 6
        self.longueur_one_room = l1
        self.largeur_one_room = l2
        self.walls = walls

    def is_possible(self):
        table_walls = self.walls.create_wall()
        if coordinates[0] == table_walls[0]:
    
class Area:
    
    def __init__(self, coordinates,floor, l1, l2):
        self.coordinates = coordinates
        self.floor = floor
        self.nb_rooms_max = 40
        self.place = Building(self.floor, self.nb_rooms_max)
        self.nb_rooms_max_longueur = 6
        self.nb_rooms_max_largeur = 6
        self.longueur_one_room = l1
        self.largeur_one_room = l2
        
    # def set_place_building_2(self):
    #     table_coordinates = self.place.get_space()
    #     #compteur = 0
    #     #for i in range(len(table_coordinates[self.floor])):
    #         #print(table_coordinates[self.floor][i])
    #     print(table_coordinates[self.floor][self.coordinates[0]][self.coordinates[1]])
    #     if np.all((table_coordinates[self.floor][self.coordinates[0]][self.coordinates[1]]) == [0,0,0,0]): #np.all pour que toutes les valeurs doivent être égales.
    #         table_coordinates[self.floor][self.coordinates[0]][self.coordinates[1]] = self.coordinates
    #         print("Set the room ok")
    #     else:
    #         print("Room occupied")
    #     return(table_coordinates)

    def set_place_building(self):
        table_coordinates = self.place.get_space()[self.floor]
        #compteur = 0
        #for i in range(len(table_coordinates[self.floor])):
            #print(table_coordinates[self.floor][i])
        print(table_coordinates[self.coordinates[0]][self.coordinates[1]])
        if np.all((table_coordinates[self.coordinates[0]][self.coordinates[1]]) == [0,0,0,0]): #np.all pour que toutes les valeurs doivent être égales.
            table_coordinates[self.coordinates[0]][self.coordinates[1]] = self.coordinates
            print("Set the room ok")
        else:
            print("Room occupied")
        return(table_coordinates)

    def set_many_places_building(self,table_many_coordinates):
        n = len(table_many_coordinates)
        table_coordinates = self.place.get_space()[self.floor]
        for i in range(n):
            table_coordinates = self.set_place_building(table_many_coordinates[i])
        return(table_coordinates)
    
    # def sort_agencement(self):
    #     table_coordinates = self.set_place_building
    #     indice_floor_trie = np.argsort(table_coordinates[self.floor], axis = 0)
    #     table_trie_abscisse = np.zeros((nb_rooms_max,4))
    #     table_trie_ordonne = np.zeros((nb_rooms_max,4))
    #     indice_non_nul = 0
    #     while(indice_floor_trie == [0,0,0,0]):
    #         indice_non_nul += 1
    #     for i in range(indice_non_nul,nb_rooms_max):
    #         table_trie_abscisse[i] = table_coordinates[floor][indice_floor_trie[indice_non_nul+i][0]]
    #         table_trie_ordonne[i] = table_coordinates[floor][indice_floor_trie[indice_non_nul+i][2]]
    #     return(table_trie_abscisse,table_trie_ordonne)
            
    # def sort_agencement(self):
    #     table_coordinates = self.set_place_building
    #     tableau_trie = np.zeros((self.nb_rooms_max_longueur,self.nb_rooms_max_largeur,4))
    #     for i in range(self.nb_rooms_max_longueur):
    #         for j in range(self.nb_rooms_min_longueur):
    #             abscisse_gauche = table_coordinates[self.floor][i][0] #Consider for now that all rooms have same size
    #             ordonne_gauche = table_coordinates[self.floor][i][1]
    #             if table_coordinates[self.floor][i] != [0,0,0,0]:
    #                 number_room_abscisse = abscisse_gauche / self.longueur_one_room
    #                 number_room_ordonne = ordonne_gauche / self.largeur_one_room
    #                 tableau_trie[number_room_abscisse][number_room_ordonne] = table_coordinates[i][j]
    #     return(tableau_trie)
    
    # def possible_agencement(self):
    #     table_trie = self.sort_agencement
    #     abscisse_area_gauche = self.coordinates[0]
    #     ordonne_area_gauche = self.coordinates[2]
    #     number_room_abscisse = abscisse_area_gauche / self.longueur_one_room
    #     number_room_ordonne = ordonne_area_gauche / self.largeur_one_room
    #     return(table_trie[number_room_abscisse][number_room_ordonne] == [0,0,0,0])

    # def possible_arrangement(self,arrangement):
    #     N_lenght, N_height, _ = np.shape(arrangement)
    #     for i in range(N_lenght):
    #         for j in range(N_height): #chech on the height first
                
    def put_arrangement_building(self,arrangement):
        #place_building = self.place.get_space()
        #place_building[self.floor] = arrangement
        return(arrangement)
                
                
        
class Room(Area):
    
    def __init__(self, coordinates,floor,l1,l2):
        self.coordinates = coordinates
        self.floor = floor
        self.nb_rooms_max = 40
        self.place = Building(self.floor, self.nb_rooms_max)
        self.nb_rooms_max_longueur = 6
        self.nb_rooms_max_largeur = 6
        self.longueur_one_room = l1
        self.largeur_one_room = l2

    def get_coordinates(self):
        return(self.coordinates)
        
class Outside(Area):
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name
        
class Corridor(Area):
    
    def __init__(self, coordinates,name):
        self.coordinates = coordinates
        self.name = name    
    
B = Building(40,1)
bb = B.get_place_areas(40)
Ar = Area([2,4,2,2], 1, 2,2)
aa = Ar.set_place_building()

cc = B.change_arrangement(aa,1)

dd = B.get_space()

El = Element([3,5,3,0],1,1,1)

ee = El.set_place_building()

ff = B.change_arrangement_element(ee,1)

gg = B.get_space_element()

room = Room([1,1,2,2],2,2,2)

hh = room.set_place_building()

B.change_arrangement(hh,2)

ii = B.get_space()

walls1 = Wall(room)

Walls2 = walls1.create_wall()


