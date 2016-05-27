import netifaces as nf
import sys
import time
import os

def print_user(network, mask):
	if network and mask != 0:
		os.system('nbtscan ' + network + '/' + mask)

def get_network(ip, netmask):
    i1, i2, i3, i4 = ip
    m1, m2, m3, m4 = netmask
    return i1 & m1, i2 & m2, i3 & m3, i4 & m4

def str_to_ip(ip):
    a, b, c, d = ip.split('.')
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

try:
	print("[!] Interfaces disponible :")
	for x in nf.interfaces():
		print("-> " + x)
	interface = raw_input("\n[*] Choisir une interface : ")
	rec_ip = nf.ifaddresses(interface)[2][0]['addr']
	rec_netmask = nf.ifaddresses(interface)[2][0]['netmask']
	ip = str_to_ip(rec_ip)
	netmask = str_to_ip(rec_netmask)
	mask_id = get_mask_id(netmask)
	network = get_network(ip, netmask)
except KeyboardInterrupt:
	print ("\n[*] Interruption voulu par l'utilisateur")
	print ("[*] Exit ...")
	sys.exit(1)

print '\n[*] Mise en place du listing des IPs dans le reseau ' + (ip_to_str(network)) + '/' + str(mask_id)
print_user((ip_to_str(network)), str(mask_id))
