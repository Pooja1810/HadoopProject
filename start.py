#!/usr/bin/python

import os,time,commands,sys,socket,getpass

print "\t\t****************************************"
print "\t\tCongrats you are in the world of data !!"
print "\t\t****************************************"

time.sleep(2)

user=raw_input("Enter user name to access project : ")
password=getpass.getpass("Enetr user password : ")

#To check user validity.
if user == 'root' and password == 'redhat' :

	print "\n\t\t\tACCESS GRANTED :-)"
	execfile('menu.py')
else :
	print "wrong authentication !!"
	exit()
