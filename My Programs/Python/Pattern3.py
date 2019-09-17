# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:42:49 2019

@author: admin
"""

n=int(input("Enter te value of n: "))
k=0
if n>0:
    for i in range(1,n+1):
        print()
        for j in range(i):
            k+=1
            print(k,end=" ")
        for j in range(i,n):
            print('*',end=" ")
else:
    for i in range(1,-n+1):
        print()
        l=k
        k+=i
        for j in range(-n-i):
            print('*',end=" ")
        for j in range(i):
            print(k,end=" ")
            k-=1
        k+=i

# The Output will be:
#    Enter the value of n: 4
#        1 * * *
#        2 3 * *
#        4 5 6 *
#        7 8 9 10
#    Enter the value of n: -4
#        * * * 1
#        * * 3 2
#        * 6 5 4
#        10 9 8 7