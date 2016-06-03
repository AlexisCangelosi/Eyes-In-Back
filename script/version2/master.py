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
    main.set("")
    attack.set("")
def List_user_auto():
	os.system('rm scan_list')
	os.system('rm interfaces')
	main.set(os.system('python3 interface_list_user2.py'))
	file = open('scan_list', 'r')
	main.set(file.read())
	file.close()
def List_user_man():
	os.system('rm scan_list')
	main.set(os.system('python3 interface_list_user.py'))
	file = open('scan_list', 'r')
	main.set(file.read())
	file.close()
def Attack_user():
	attack.set("coucou tu es attaquer :)")
def About():
    main.set("This is a simple example of a menu")



# ----- INTERFACE ----- #

root = Tk()
root.title("EIB")
root.geometry("1280x800")
menu = Menu(root)
root.config(menu=menu)

main = StringVar()
attack = StringVar()

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

actionmenu = Menu(menu)
menu.add_cascade(label="Action", menu=actionmenu)
actionmenu.add_command(label="List network auto", command=List_user_auto)
actionmenu.add_command(label="List network manuel", command=List_user_man)
actionmenu.add_command(label="Attack user", command=Attack_user)



helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

fichier_open = ttk.Label(root, textvariable=main)
fichier_open.pack()
print_attack = ttk.Label(root, textvariable=attack)
print_attack.pack()


mainloop()

