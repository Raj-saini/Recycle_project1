from csv import Dialect
from tkinter import *
from PIL import ImageTk,Image  #Python Imaging Library and it adds image processing to Python
import sqlite3
from openpyxl import load_workbook

root = Tk()
root.title("Recycle Rewards")
root.geometry("600x600")
root.config(bg='#E4DA98')
root.photo = ImageTk.PhotoImage(Image.open("images.png"))
#root.workbook = load_workbook(filename="rewards.xlsx")
#root.sheet = root.workbook.active

# Database

#Create a database and connect
conn = sqlite3.connect('recycle_rewards.db')

# Create cursor
c = conn.cursor()

# Create table

c.execute(""" CREATE TABLE IF NOT EXISTS reward_details(Barcode text,
        Product_Name text, 
        Product_Type text, 
        Product_quantity integer, 
        Points integer, 
        Total_Rewards integer)""" )


    #create save function
def save():
    #Create a database and connect
    conn = sqlite3.connect('recycle_rewards.db')
    # Create cursor
    c = conn.cursor()
    # insert into the table
    c.execute("INSERT INTO reward_details VALUES (:bar, :name, :type, :qty, :epoints, :trewards)",
            {
                'bar': bar.get(),
                'name': name.get(),
                'type': type.get(),
                'qty' : qty.get(),
                'epoints': epoints.get(),
                'trewards': trewards.get()
            })

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

        #clear the textboxes
    bar.delete(0, END)
    name.delete(0, END)
    type.delete(0, END)
    qty.delete(0, END)
    epoints.delete(0, END)
    trewards.delete(0, END)



 # create reset function 
def reset():
        #clear the textboxes
        bar.delete(0, END)
        name.delete(0, END)
        type.delete(0, END)
        qty.delete(0, END)
        epoints.delete(0, END)
        trewards.delete(0, END)

def search():

    #Create a database and connect
    conn = sqlite3.connect('recycle_rewards.db')

    # Create cursor
    c = conn.cursor()

    # search the data
    c.execute("SELECT *, oid FROM reward_details")
    records = c.fetchall()
    #print(records)
    #print_records
    # fetch results
    print_records = ''
    for record in records:
       print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " "+ str(record[4]) + " "+ str(record[5]) + "\n"
       with open("rewards.xlsx", mode='w') as file:
            file.write("Records " + print_records)   

    search_label = Label(root, text=print_records)
    search_label.grid(row=9, column=0, columnspan=5, rowspan=6, sticky='NSEW')
    
                     

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return

'''

    # create records display function 
def display():

    #Create a database and connect
    conn = sqlite3.connect('recycle_rewards.db')

    # Create cursor
    c = conn.cursor()

    # search the data
    c.execute("SELECT *, oid FROM reward_details")
    records = c.fetchall()
    #print(records)
    #print_records
    # fetch results
    print_records = ''
    with open('customer_rewards.csv', 'a') as f:
            w = csv.writer(f, dialect='excel')
            for record in records: 
                w.writerow(record) 


    search_label = Label(root, text=print_records)
    search_label.grid(row=9, column=0, columnspan=5, rowspan=6, sticky='NSEW')
       #print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " "+ str(record[4]) + " "+ str(record[5]) + "\n"
        
                 

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return
'''

# Create the graphical interface

heading = Label(root, text='Recycle Rewards', fg='maroon', bg='#E4DA98',
                              font=('Arial', 20, 'bold'))
barcode = Label(root, text='Product Barcode', fg='maroon', bg='#E4DA98', font=('NONE', 14))
bar = Entry(root)
product_name = Label(root, text='Product Name', fg='maroon', bg='#E4DA98', font=('NONE', 14))
name = Entry(root)
       
product_type = Label(root, text='Product Type', fg='maroon', bg='#E4DA98', font=('NONE', 14))
type = Entry(root)
        # insert(0, 'Enter product qty')
product_quantity = Label(root, text='Product Quantity', fg='maroon', bg='#E4DA98', font=('NONE', 14))
qty = Entry(root)
        # points.insert(0, 'Enter points')
points = Label(root, text='Points', fg='maroon', bg='#E4DA98', font=('NONE', 14))
epoints = Entry(root)
        # rewards.insert(0, 'Enter rewards')
rewards = Label(root, text='Total Rewards', fg='maroon', bg='#E4DA98', font=('NONE', 14))
trewards = Entry(root)
        
        # create buttons to save, reset and search
save_btn = Button(root, text='Save', bg='maroon', fg='#E4DA98', activebackground='red', height=1,
                                  width=8, bd=5, font=('NONE', 18), command=save)
reset_btn = Button(root, text='Reset', bg='maroon', fg='#E4DA98', activebackground='red',
                                   height=1, width=8, bd=5, font=('NONE', 18), command=reset)
search_btn = Button(root, text='Search', bg='maroon', fg='#E4DA98', activebackground='red',
                                    width=8, bd=5, font=('NONE', 18), command=search)
title1 = Label(root, text='Programmed by Jimmy,Bipin,Rajbeer&Neha', fg='maroon', bg="#E4DA98",
                               font=('NONE', 12))
image_label = Label(image=root.photo)

        # bind all events
heading.grid(row=0, column=0, columnspan=2, sticky='w')

barcode.grid(row=1, column=0, sticky='w')
bar.grid(row=1, column=1, sticky='w')

product_name.grid(row=2, column=0, sticky='w')
name.grid(row=2, column=1, sticky='w')

product_type.grid(row=3, column=0, sticky='w')
type.grid(row=3, column=1, sticky='w')

product_quantity.grid(row=4, column=0, sticky='w')
qty.grid(row=4, column=1, sticky='w')

points.grid(row=5, column=0, sticky='w')
epoints.grid(row=5, column=1, sticky='w')

rewards.grid(row=6, column=0, sticky='w')
trewards.grid(row=6, column=1, sticky='w')

      
save_btn.grid(row=7, column=0,  columnspan=2,  sticky='ws')
reset_btn.grid(row=7, column=1,  columnspan=2, sticky='es')
search_btn.grid(row=7, column=2, columnspan=3, sticky='ws')

title1.grid(row=8, column=3, sticky='w')

image_label.grid(row=1, column=3, rowspan=5)


 # binding button widgets events
#save_btn.bind('<Button-1>',save)
#reset_btn.bind('<Button-1>', reset)
#search_btn.bind('<Button-1>',search)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()










