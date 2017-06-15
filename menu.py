#!/usr/bin/python

import os,time,commands,sys,socket

options="""
press 1 to setup Hadoop Cluster :
press 2 to setup MR :
press 3 to setup HIVE:
"""
print options 

#ch for  storing options

user_choice=raw_input()

print "-------------------------------------------"

if user_choice == '1' :
	print "ok get ready to start hadoop cluster"
	print "------------------------------------"
	execfile('hdfs_setup.py')

elif user_choice == '2' :
	print "make sure you have enough amount to CPU cores"
	print "--------------------------------------------"
	execfile('mrsetup.py')

else :
	print "wrong option"
	execfile('startpr.py')
