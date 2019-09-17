# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:56:08 2019

@author: admin
"""

n=int(input("Enter the value: "))
k=0
for i in range(1,n+1):
        print()
        k+=i
        for j in range(n-i):
            print('*',end=" ")
        for j in range(i):
            print(k,end=" ")
            k-=1

# The Output will be:
#    Enter the value: 5
#
#       * * * * 1
#       * * * 2 1
#       * * 3 2 1
#       * 4 3 2 1
#       5 4 3 2 1