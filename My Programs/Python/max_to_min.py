# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:51:10 2019

@author: admin
"""

l=input().split( )                # We can also use 
a=int(l[0])                        #  list(map(int,input().split( )))
for i in range(1,len(l)):
    if int(l[i])>a:
        a=int(l[i])
b=int(l[0])
for i in range(1,len(l)):
    if int(l[i])<b:
        b=int(l[i])
for i in range(a,b-1,-1):
    print(i,end=" ")




# 5 8 2

## 8 7 6 5 4 3 2