# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:36:16 2019

@author: admin
"""

a=input().split( )
for i in range((len(a)-1),0,-1):
    for j in range(i-1,0,-1):
        if a[i]==a[j]:
            a.pop(i)
            a.append('*')
for i in range(1,len(a)):
    if a[0]==a[i]:
        a.pop(i)
        break
for i in a:
    count=a.count('*')
    for j in range(len(a)-1,len(a)-count-1,-1):
        a.pop(j)
print(' '.join(a))



# 1 2 2 3 5 2 5 6 8
## 1 2 3 5 6 8