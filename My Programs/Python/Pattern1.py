# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:30:04 2019

@author: admin
"""

n,p=map(int,input().split( ))
for i in range(1,n+1):
    if i<=p:
        for j in range(i*2):
            print(i,end=" ")
    else:
        for j in range(i):
            print(i,end=" ")
    print()



# 6 3

## 1 1
## 2 2 2 2
## 3 3 3 3 3 3
## 4 4 4 4
## 5 5 5 5 5
## 6 6 6 6 6 6

#### Here the number of times the numbers less than or equal to p,that is, 1,2,3(here) is 2*that number ####
#### that is 1 is printed 2 times, 2 is printed 4 times, 3 is printed 6 times ####
#### Then the remaining numbers till n,that is, 4,5,6(here) are printed upto 4, 5 and 6 times respectively ####