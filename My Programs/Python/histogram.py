# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:01:27 2018

@author: admin
"""

d={}
string=input("Enter ")
for i in string:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)



# aedefffgh

## {'a':1,'e':2,'d':1,'f':3,'g':1,'h':1}