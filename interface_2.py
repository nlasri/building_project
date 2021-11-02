from tkinter import *

root = Tk()
root.title("Entry Boxes")
root.geometry("700x500")
root.configure(background='LightSteelBlue2')

my_entries = {}

def generate_building():
    print('room')
    print(my_entries)


title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')

title.grid(row = 0, columnspan = 6, sticky = 'nesw')

element=['Floor', 'Room', 'Element']
for y in range(1,4):
    my_label = Label(root, text=element[y-1], bg='Dodger Blue')
    my_label.grid(row=y, column=0, pady=20, sticky = 'nesw')
    my_entries[element[y-1]]=[]
    for x in range(1,5):
        my_entry = Entry(root)
        my_entry.insert(0, element[y-1] + str(x))
        my_entry.grid(row=y, column=x, pady=20, padx=5)
        my_entries[element[y-1]].append(my_entry.get())

my_button = Button(root, text="Create my building", command=generate_building, bg='lightsteelblue4')
my_button.grid(row=6, column=0, pady=20)


root.mainloop()