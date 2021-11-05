# building_project
Authors : Alain Tran, Narjisse Lasri

# Subject
This project allows the creation of a digital twin.

# How it works

## Creation of the building
To create a digital twin, the user has to execute the file "builder.py". This file will generate an interface to create a building :

![image](https://user-images.githubusercontent.com/60067281/140500528-80538eaf-2a48-472f-884b-8f55e1d4f12a.png)

The user enters the following information : 
  * Width of the building (float)
  * Height of the building (float)
  * Number of floors (integer) : if 0 there is only a ground floor.

Once the user is happy with its inputs, he can create the building by clicking on "Create my building".

## Creation of areas and elements
Once the building is created. A second interface is generated :

![image](https://user-images.githubusercontent.com/60067281/140500991-7f1303eb-5541-4f46-87a5-27c23b6925d0.png)

The interface allows the user to add areas and element.
Each area/element can be added with the following information:
  * Coordinate x (float)
  * Coordinate y (float)
  * Width of the building (float)
  * Height of the building (float)
  * Floor in which the area/element will be added (integer)

If the user wants to add elements to the areas, he must do so at the same time as he creates the areas. Indeed, an element is automatically added to the last created area of the floor.

**Warning!** The user must follow the following rules :
  * The area added has to be in the building (if not a message of error will be displayed in the prompt).
  * An element added to an area has to be in the area (if not a message of error will be displayed in the prompt).

  * An area added must not be position on another area (if not a message of error will be displayed in the prompt).
  * An element added to and area must not be position on another element of this area (if not a message of error will be displayed in the prompt).

## More features
The user can choose two different design:
  * High design : 
This design use rectangle of colors to represent areas and its elements.
A thickness of 0.5 is assigned to the element door (which has normally a zero thickness).
This design is automatically choosen.

  * Medium design : 
This design use lines of colors to represent the areas of the building.
In this design, the elements aren't representated.
To choose this design, the user has to replace "high_design" by "medium_design" in the file "builder.py" in the part "if __name__ == "__main__":".

## Saving the building
During the creation of the building, the building is automatically saved. The user can work on the building later to add/delete areas or add alements. For that, the user can use the file "final_building.py".

## Kmeans and Graham
Now that the building is created and modeled, the user will be able to detect clusters of people in the building. In order to do that, the user can use the file "cluster.py" that has the implementation of the Kmeans and Graham convex envelope method. In particular, the user can use the show_cluster function that plot show people coordinates and group them according to their clusters (these clusters will be delimited thanks to the Graham convex envelope).
