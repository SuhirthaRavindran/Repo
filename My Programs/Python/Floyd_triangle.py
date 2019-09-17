# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:39:40 2019

@author: admin
"""

n=int(input("Enter number of rows: "))
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()


# The Output is:
#       Enter number of rows: 4
#       1
#       2 3
#       4 5 6
#       7 8 9 10