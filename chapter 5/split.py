#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import os
import sys
def split(filename,n):
 #filepath= path=os.path.abspath(os.path.join(directory, filename))
 f=open(filename,'r')
 text=f.readlines()
 j=1
 i=0
 lng=len(text)
 while i <lng:
   fname='file%d'% j
   print fname
   i+=n
   j+=1
   index = open(os.path.join('test', fname), 'a')
   for k in text[:n]:
      index.write(k)
   index.close()
   text=text[n:]

split('problem2.py',3)
