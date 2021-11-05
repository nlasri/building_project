import pickle 
from classes import *
from builder import *
import os

if os.path.getsize('building.obj') > 0:      
    with open('building.obj', "rb") as f:
        unpickler = pickle.Unpickler(f)
        building_import = unpickler.load()
else:
    print("empty")

print(building_import.areas)