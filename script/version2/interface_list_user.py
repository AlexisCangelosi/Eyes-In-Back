#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTS
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
import sys
import os

#---- Fonctions ----

def print_user(*args):
	try:
		value = str(network.get())
		os.system('nbtscan ' + value + ' > scan_list')
		showinfo('Status', 'Scan terminé !')
		root.destroy()
	except ValueError:
		pass
	
	
#---- Interface Graphique ----

# Création de l'interface
root = Tk()
root.title('List user 1.0')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Déclaration des variables
network = StringVar()
scan = StringVar()

# Mise en place de l'interface

# NETWORK
ttk.Label(mainframe, text="Network/Mask : ").grid(column=1, row=1, sticky=E)

network_entry = ttk.Entry(mainframe, width=20, textvariable=network)
network_entry.grid(column=2, row=1, sticky=(W, E))

# SEARCH
ttk.Button(mainframe, text="Search", command=print_user).grid(column=3, row=1, sticky=W)

# RESULT
ttk.Label(mainframe, textvariable=scan).grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

network_entry.focus()
root.bind('<Return>', print_user)

root.mainloop()



