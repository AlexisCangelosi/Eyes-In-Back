#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTS
from tkinter import *
from tkinter import ttk
import netifaces as nf
import sys
import os

#---- Fonctions ----

def print_user(*args):
	try:
		value = str(choix_iface.get())
		rec_ip = nf.ifaddresses(value)[2][0]['addr']
		rec_netmask = nf.ifaddresses(value)[2][0]['netmask']
		ip = str_to_ip(rec_ip)
		netmask = str_to_ip(rec_netmask)
		mask_id = get_mask_id(netmask)
		mask = int(mask_id)
		network = get_network(ip, netmask)
		nw = ip_to_str(network)
		os.system('nbtscan ' + nw + '/' + str(mask) + ' > scan_list')
		file = open('scan_list', 'r')
		scan.set(file.read())
		file.close()
	except ValueError:
		pass

def list_interface():
	os.system('echo "" > interfaces')
	for x in nf.interfaces():
		os.system('echo ' + x + ' >> interfaces')
	file = open('interfaces', 'r')
	interface.set(file.read())
	file.close()


	
def get_network(ip, netmask):
    i1, i2, i3, i4 = ip
    m1, m2, m3, m4 = netmask
    return i1 & m1, i2 & m2, i3 & m3, i4 & m4

def str_to_ip(ip):
    a, b, c, d = ip.split('.')
    d = 0
    return int(a), int(b), int(c), int(d)

def ip_to_str(ip):
    return '{}.{}.{}.{}'.format(*ip)

def get_mask_id(ip):
	i1, i2, i3, i4 = ip
	e1 = (i1+1) / 8
	e2 = (i2+1) / 8
	e3 = (i3+1) / 8
	e4 = (i4+1) / 8
	mask_id = (e1 + e2 + e3 + e4) / 4
	return mask_id
	
#---- Interface Graphique ----

# Création de l'interface
root = Tk()
root.title('List user 2.0')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(W, E))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Déclaration des variables
interface = StringVar()
choix_iface = StringVar()
scan = StringVar()

# Mise en place de l'interface

# Interfaces disponible
ttk.Button(mainframe, text="Interfaces disponible", command=list_interface).grid(column=1, row=1)
ttk.Label(mainframe, textvariable=interface).grid(column=1,row=2)

# Choix interface
choix_interface = ttk.Entry(mainframe, width=7, textvariable=choix_iface).grid(column=1,row=3)
ttk.Button(mainframe, text='Search', command=print_user).grid(column=1,row=4)

ttk.Label(mainframe, textvariable=scan).grid(column=1, row=5)

ttk.Button(mainframe, text='Quit', command=root.destroy).grid(column=1,row=6)

#Fin de l'interface
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', print_user)

root.mainloop()



