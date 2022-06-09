# Import tkinter import necessary modules

from tkinter import *
import sqlite3
from tkinter import ttk

main_window = Tk()

# Making the database

# Create the database table
conn = sqlite3.connect("People_info.db")

# Create the cursor/executor
c = conn.cursor()

# Create the table
'''
c.execute("""CREATE TABLE info (
        Name text,
        Item text,
        Amount integer)

""")
'''

# The quit button function
def exit():
    main_window.destroy()

# Building the GUI
Quit = Button(main_window, text="Quit", command=exit, height=3, width=8).place(x=80, y=80)

# Entry Label
main_Label = Label(main_window, text="Julie Part Hire store", font=("Courier", 30)).place(x=50, y=10)

# Building the Labels

Customer_name_label = Label(main_window, text="Customer name: ").place(x=25, y=175)
Item_label = Label(main_window, text="Item: ").place(x=25, y=205)
Amount_label = Label(main_window, text="Amount: ").place(x=25, y=235)
Delete_label = Label(main_window, text="Delete: ").place(x=400, y=190)

# Building the entries
Customer_name_entry = Entry(main_window)
Customer_name_entry.place(x=125, y=175)
Delete_entry = Entry(main_window)
Delete_entry.place(x=475, y=190)

# Create spinbox for amount
amount = StringVar()
amount_entry = Spinbox(main_window, from_=1, to=50, textvariable=amount, wrap=False, state='readonly').place(x=125, y=235)

# Create combobox for the items
item = StringVar()
items = ['Bar', 'Bar fridge', 'Chair', 'Coffee Plunger', 'Bowl', 'Plate', 'Bucket', 'Knife']
item_entry = ttk.Combobox(main_window, textvariable=item, state='readonly', value=items).place(x=125, y=205)

# Commit the changes to the database
conn.commit()

# Close the database
conn.close()

main_window.geometry("650x650")
main_window.mainloop()

# The rows/tables I would have in the database
# Name datatype = String
# Item hired = String
# Amount hired = Integer
# Item = Combobox
# Amount = spinbox
