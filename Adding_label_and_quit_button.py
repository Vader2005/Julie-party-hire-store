# Import tkinter import necessary modules

from tkinter import *
import sqlite3

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


# Commit the changes to the database
conn.commit()

# Close the database
conn.close()

main_window.geometry("600x600")
main_window.mainloop()

# The rows/tables I would have in the database
# Name datatype = String
# Item hired = String
# Amount hired = Integer
