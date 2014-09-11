# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

import sys
def files(filenames):
  for filename in filenames:	
	  f=open(filename,'r')
	  text=f.readlines()
	  for i in text:
	    if len(i)> 40:
	     print i

files(sys.argv[1])
