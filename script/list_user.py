import sys
import time
import os

try:
	ip = raw_input("[*] Choisir une IP : ")
	reseau = raw_input("[*] Choisir un masque : ")
except KeyboardInterrupt:
	print "\n[*] Interruption voulu par l'utilisateur"
	print "[*] Exit ..."
	sys.exit(1)
print '\n[*] Mise en place du listing des IPs dans le reseau ' + ip + '/' + reseau

def print_user(ip, reseau):
	if ip and reseau != 0:
		os.system('nbtscan ' + ip + '/' + reseau)


print_user(ip, reseau)
