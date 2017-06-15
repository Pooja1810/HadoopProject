#!/usr/bin/python

import os,time,commands,sys,socket,getpass

print "\t\t\t****************************************"
print "\t\t\tCongrats you are in the world of data !!"
print "\t\t\t****************************************"

time.sleep(2)

user=raw_input("Enter user name to access project : ")
password=getpass.getpass("Enetr user password : ")

print "-----------------------------------------------"

if user == 'root' and password == 'redhat' :

	print "\t\t\tACCESS GRANTED :-)"
	execfile('menu.py')
else :
	print "wrong authentication !!"
	exit()
