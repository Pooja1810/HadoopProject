#!/usr/bin/python 

import os,commands,time,sys,socket

options="""
Press 1 to manual setup hadoop cluster :
Press 2 to automatic setup hadoop cluster :
"""
print options 

ch=raw_input()

print "-----------------------------------------------"

if ch == '1':
	print "good choice.... "
	print "Firstly we'll scan CPU core and RAM info"
	print "----------------------------------------"
	execfile('scan.py')
else :
	print "bad choice"
	print "----------------------------------------"
	execfile('menu.py')
