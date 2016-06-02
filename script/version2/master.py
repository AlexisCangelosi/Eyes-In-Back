#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----- IMPORTS ----- #

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import netifaces as nf
import sys
import os

# ----- FONCTIONS ----- #

def NewFile():
    print ("New File!")
    main.set("")
def List_user():
	main.set(os.system('python3 interface_list_user2.py'))
	file = open('scan_list', 'r')
	main.set(file.read())
	file.close()

def About():
    print ("This is a simple example of a menu")



# ----- INTERFACE ----- #

root = Tk()
root.geometry("1280x800")
menu = Menu(root)
root.config(menu=menu)

main = StringVar()

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

listmenu = Menu(menu)
menu.add_cascade(label="List User", menu=listmenu)
listmenu.add_command(label="List user", command=List_user)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

fichier_open = ttk.Label(root, textvariable=main)
fichier_open.pack()

mainloop()

