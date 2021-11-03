from tkinter import *
from builder import generate_building


def generate_interface(building_created):

    #Intro
    root = Tk()
    root.title("Entry Boxes")
    root.geometry("900x500")
    root.configure(background='LightSteelBlue2')
    title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
    title.grid(row = 0, columnspan = 6, sticky = 'nesw')

    #Selection
    my_label = Label(root, text='Element', bg='Dodger Blue')
    my_label.grid(row=1, column=0, pady=20, sticky = 'nesw')
    my_entries=[]

    #Kind
    OptionList = ["Area","Room","Corridor","Door", "Outside","Element"] 
    variable = StringVar(root)
    variable.set(OptionList[0])
    opt = OptionMenu(root, variable, *OptionList)
    opt.grid(row=1, column=1, pady=20, padx=5)
    my_entries.append(variable)

    #Coordinates and measures
    label = ['coordinate x', 'coordinate y', 'width', 'height', 'floor']
    for x in range(2,7):
        my_entry = Entry(root)
        my_entry.insert(0, label[x-2])
        my_entry.grid(row=1, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

    #button
    my_button = Button(root, text="Create my building", command= lambda: generate_building(my_entries, building_created), bg='lightsteelblue4')
    my_button.grid(row=6, column=0, pady=20)

    root.mainloop()




