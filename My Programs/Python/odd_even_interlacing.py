# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:35:58 2019

@author: admin
"""

def list_order(maxi,mini):            # Always define the function at starting of the program
    for j in range(len(maxi)):
        print(maxi[j],end=" ")
        if j<len(mini):
            print(mini[j],end=" ")

a=int(input())
b=int(input())
odd=[]
even=[]
for i in range(a,b+1):
    if i%2!=0:
        odd.append(i)
for i in range(b,a-1,-1):
    if i%2==0:
        even.append(i)
if len(odd)>=len(even):
    list_order(odd,even)
else:
    list_order(even,odd)


### case 1: length of odd numbers > length of even numbers

# 5
# 11

## 5 10 7 8 9 6 11

#Explanation:
    # odd numbers from 5 to 11 is 5 7 9 11
    # even numbers from 11 to 5 is 10 8 6
    # interlacing starts with odd number


### case 2: length of even numbers > length of odd numbers

# 4
# 14

## 14 5 12 7 10 9 8 11 6 13 4

#Explanation:
    # even numbers from 14 to 4 is 14 12 10 8 6 4
    # odd numbers from 4 to 14 is 5 7 9 11 13
    ## interlacing starts with even number


### case 3: length of even numbers = = length of odd numbers
    # interlacing starts with odd number