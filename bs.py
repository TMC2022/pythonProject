# import random
# import tkinter as tk
# import sqlite3 as sq
# #
#
#
#
# root = tk.Tk()
#
# def button():
#     conn = sq.connect('contacts.db')
#     contact = [random.Random(), number.get(), mess.get()]
#     c = conn.cursor()
#     c.execute('''INSERT INTO contacts VALUES (?,?,?)''', contact)
#     conn.commit()
#     conn.close()
#     print(mess.get())
#
# # canvas
# canvas = tk.Canvas(root, width=400, height=200)
# canvas.grid(rowspan=6, columnspan=6)
#
# #number box
# numberlabel = tk.Label(text='Number')
# numberlabel.grid(row=0, column=0)
# number = tk.Entry(root, )
# number.grid(row=0, column=2, rowspan=1)
#
# #message box
# messlabel = tk.Label(text='Message')
# messlabel.grid(row=2, column=0)
# mess = tk.Entry(root,)
# mess.place(y=40, x=120, height=100, width=200)
#
# #button
# button1 = tk.Button(root, command=button, text='Send SMS' )
# button1.grid(row=4, column=0)
#
# root.mainloop()
from bs4 import BeautifulSoup
import urllib.request
import html5lib
with open('index.html', 'r') as f:

# doc = urllib.request.urlopen('https://www.pornhub.com')
    soup = BeautifulSoup(f, 'html5lib')
    soup.name = "thomas"

    print(soup.prettify())

# print(soup.find_all('/view_video.php'))
# with open('index.html', 'w') as f:
#     # soup = BeautifulSoup(f)
#     f.write(str(soup))
#     f.close()
