# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:31:25 2019

@author: admin
"""

n=int(input("Enter the value of n: "))
k=2
l=n-1
for i in range(1,n+1):
    print(i,end=" ")
print()
for i in range(n-2):
    print(k,end=" ")
    k+=1
    for j in range(n-2):
        print('*',end=" ")
    print(l)
    l-=1
for j in range(n,0,-1):
    print(j,end=" ")


# The Output will be:
#    Enter the value of n: 4
#      1 2 3 4
#      2 * * 3
#      3 * * 2
#      4 3 2 1
#
#    Enter the value of n: 5
#      1 2 3 4 5
#      2 * * * 4
#      3 * * * 3
#      4 * * * 2
#      5 4 3 2 1