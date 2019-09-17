# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:07:12 2019

@author: admin
"""

n=int(input())
l=[]
count=0
for i in range(n):
    l.append(input())
e=input()
e=e.split('.')
for i in l:
    i=i.split('.')
    if i[1]==e[1] and len(i[0])>count:
        count=len(i[0])
        j='.'.join(i)
if count==0:
    print("FILE NOT FOUND")
else:
    print(j)




# 3
# skdjk.java
# ksdkas.c
# ksfst.java
# .java        # .kl

## skdjk.java  ## FILE NOT FOUND