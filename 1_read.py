# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:37:14 2019

@author: User
"""

fh = open('names.txt', 'r')
names = fh.read()
print (names)
fh.close()


list_names = names.split()
print (list_names)


for snames in list_names:
    print ("hello, " , snames)