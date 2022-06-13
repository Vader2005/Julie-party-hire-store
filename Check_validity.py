# Import tkinter import necessary modules

from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox

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

# Check for delete entry 

def Delete_validity():
    delete_check = 0

    # Make sure Delete can only be a number
    if Delete_entry.get().isalpha():
        messagebox.showerror("Error", "Delete can only take a receipt number to delete")
        delete_check = 1

    # Run the delete function if all is well

    if delete_check == 0:
        delete()

# Check validity for all entries except delete entry

def check_input():
    input_check = 0

    # Make sure customer name is not empty
    if len(Customer_name_entry.get()) == 0:
        messagebox.showerror("Error", "Customer name cannot be empty")
        input_check = 1

    # Make sure Item is not empty
    if len(item.get()) == 0:
        messagebox.showerror("Error", "Item cannot be empty")
        input_check = 1

    # Make sure amount is not empty
    if len(amount.get()) == 0:
        messagebox.showerror("Error", "Amount cannot be empty")
        input_check = 1

    # Make sure customer name can only take a string
    if Customer_name_entry.get().isdigit():
        messagebox.showerror("Error", "Customer name can only be a string")
        input_check = 1

    # Run the submit function if all is good

    if input_check == 0:
        submit()

# Building the Translate feature

def Translate():
    Language_chosen = translate.get()

    if Language_chosen == 'Te Reo Maori':
        Customer_name_label.config(text="Ingoa Kiritaki:")
        Item_label.config(text="Tūemi:")
        Amount_label.config(text="Te nui")
        Delete_label.config(text="Mukua:")
        Quit.config(text="Whakamutua")
        submit_button.config(text="tuku korero")
        print_button.config(text="Panui korero")
        delete_button.config(text="Mukua nga korero")
        Terms_button.config(text="Panui Nga Ture")
        main_Label.config(text="Toa utu paati Julie")
    elif Language_chosen == 'Samoan':
        Customer_name_label.config(text="Igoa o le tagata fa'atau:")
        Item_label.config(text="mea:")
        Amount_label.config(text="aofaiga:")
        Delete_label.config(text="Aveese: ")
        Quit.config(text="tuu")
        submit_button.config(text="Tu'u mai fa'amatalaga")
        print_button.config(text="Lolomi fa'amatalaga")
        delete_button.config(text="Ave'ese fa'amatalaga")
        Terms_button.config(text="Faitau faaupuga")
        main_Label.config(text="Faleoloa totogi a Julie party")
    elif Language_chosen == 'Northern Chinese':
        Customer_name_label.config(text="顾客姓名:")
        Item_label.config(text="物品:")
        Amount_label.config(text="数量:")
        Delete_label.config(text="删除:")
        Quit.config(text="退出")
        submit_button.config(text="提交信息")
        print_button.config(text="打印信息")
        delete_button.config(text="删除信息")
        Terms_button.config(text="阅读条款")
        main_Label.config(text="朱莉派对租用商店")
    elif Language_chosen == 'Hindi':
        Customer_name_label.config(text="ग्राहक का नाम:")
        Item_label.config(text="वस्तु:")
        Amount_label.config(text="राशि:")
        Delete_label.config(text="मिटाना:")
        Quit.config(text="छोड़ना")
        submit_button.config(text="जानकारी जमा करें")
        print_button.config(text="प्रिंट जानकारी")
        delete_button.config(text="जानकारी हटाएं")
        Terms_button.config(text="शर्तें पढ़ें")
        main_Label.config(text="जूली पार्टी भाड़े की दुकान")
    elif Language_chosen == 'English':
        Customer_name_label.config(text="Customer name:")
        Item_label.config(text="Item:")
        Amount_label.config(text="Amount:")
        Delete_label.config(text="Delete:")
        Quit.config(text="Quit")
        submit_button.config(text="Submit info")
        print_button.config(text="Print info")
        delete_button.config(text="Delete info")
        Terms_button.config(text="Read terms")
        main_Label.config(text="Julie party hire store")

# Terms and conditions

def Terms():
    result = messagebox.askquestion("Terms and conditions", """
    
    By using this application you are allowing your details to be saved for the purposes of this application.
    If you click agree then you will proceed to use the application.
    If you click no then you will close the application.
    By agreeing to use this app you agree to download and play War Robots.
    You also are agreeing to download and play Bee Swarm Simulator.
    If you proceed and don't meet those conditions you will be executed by the Tribe""")

    if result=='no':
        main_window.destroy()

# Building the delete function

def delete():
    # Connect to the database
    conn = sqlite3.connect("People_info.db")
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM info WHERE oid=" + Delete_entry.get())

    # Close the databse
    conn.commit()
    conn.close()

# Building the submit_info function

def submit():
    # connect to the cursor
    conn = sqlite3.connect("People_info.db")
    c = conn.cursor()

    # Insert the values into the database
    c.execute("INSERT INTO info VALUES (:Customer_name_entry, :amount, :item)",

            {
                'Customer_name_entry': Customer_name_entry.get(),
                'amount': amount.get(),
                'item': item.get()
            }
    
    )

    # Close the connection
    conn.commit()
    conn.close()

    # Clear all the entries
    Customer_name_entry.delete(0, 'end')
    amount.set('')
    item.set('')

# Building the print_info function

def query():
    # Connect the cursor
    conn = sqlite3.connect("People_info.db")
    c = conn.cursor()

    # Query the databse

    c.execute("SELECT *, oid FROM info")
    records = c.fetchall()

    # Loop through the database and print details
    print_record = ''

    for record in records:
        print_record += str(record[0]) + "\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\t\t" + str(record[3]) + '\n'

    display_label = Label(main_window, text=print_record).place(x=25, y=350)

    # Creating the heading Labels
    Customer_name_display_label = Label(main_window, text="Customer").place(x=25, y=300)
    Amount_display_label = Label(main_window, text="Amount").place(x=120, y=300)
    Item_label = Label(main_window, text="Item").place(x=220, y=300)
    oid_label = Label(main_window, text="Receipt").place(x=310, y=300)

    # Closing the connection
    conn.commit()
    conn.close()


# Building the GUI
Quit = Button(main_window, text="Quit", command=exit, height=3, width=16)
Quit.place(x=5, y=80)

# Entry Label
main_Label = Label(main_window, text="Julie Part Hire store", font=("Courier", 30))
main_Label.place(x=50, y=10)

# Building the Labels

Customer_name_label = Label(main_window, text="Customer name: ")
Customer_name_label.place(x=25, y=175)
Item_label = Label(main_window, text="Item: ")
Item_label.place(x=25, y=205)
Amount_label = Label(main_window, text="Amount: ")
Amount_label.place(x=25, y=235)
Delete_label = Label(main_window, text="Delete: ")
Delete_label.place(x=400, y=190)

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

# Create the submit button
submit_button = Button(main_window, text="Submit info", command=check_input, height=3, width=16)
submit_button.place(x=145, y=80)

# Create the print info button
print_button = Button(main_window, text="Print info", command=query, height=3, width=16)
print_button.place(x=275, y=80)

# Create the delete info button
delete_button = Button(main_window, text="Delete info", command=Delete_validity, height=3, width=16)
delete_button.place(x=415, y=80)

# Create the Terms and conditions button
Terms_button = Button(main_window, text="Read Terms", height=3, width=16, command=Terms)
Terms_button.place(x=570, y=80)

# Building the Translate label
Translate_label = Label(main_window, text="Translate: ").place(x=400, y=230)

# Create the combobox for the trabslate labels
translate = StringVar()
Languages = ["Te Reo Maori", "Samoan", "Northern Chinese", "Hindi", "English"]
Languages_entry = ttk.Combobox(main_window, textvariable=translate, state='readonly', value=Languages).place(x=475, y=230)

# Translate button
Translate_button = Button(main_window, text="Translate", height = 3, width=8, command=Translate).place(x=490, y=270)


# Commit the changes to the database
conn.commit()

# Close the database
conn.close()

main_window.geometry("800x800")
main_window.mainloop()

# The rows/tables I would have in the database
# Name datatype = String
# Item hired = String
# Amount hired = Integer
# Item = Combobox
# Amount = spinbox
