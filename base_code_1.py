# Import tkinter import necessary modules

from tkinter import *
import sqlite3

# Making the database

# Create the database table
conn = sqlite3.connect("People_info.db")

# Create the cursor/executor
c = conn.cursor()

# Create the table

c.execute("""CREATE TABLE info (
        Name text,
        Item text,
        Amount integer)

""")

# Commit the changes to the database
conn.commit()

# Close the database
conn.close()

# The rows/tables I would have in the database
# Name datatype = String
# Item hired = String
# Amount hired = Integer
