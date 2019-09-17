# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:17:27 2019

@author: admin
"""

n=int(input("Enter the value: "))
a=n
l=-1
k=0
for i in range(a):
    for j in range(a-1):
        print('-',end="")
    a-=1
    print('<',end="")
    for j in range(l+2):
        print(k,end="")
        k+=1
        if k==10:
            k=0
    l+=2
    print('>')
for i in range(n-1):
    for j in range(a+1):
        print('-',end="")
    a+=1
    print('<',end="")
    for j in range(l-2):
        print(k,end="")
        k+=1
        if k==10:
            k=0
    l-=2
    print('>')


## The output will be:
    
    # Enter the value: 4
    
    # ---<0>
    # --<123>
    # -<45678>
    # <9012345>
    # -<67890>
    # --<123>
    # ---<4>