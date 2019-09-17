# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:58:44 2019

@author: admin
"""

for i in range(int(input("Enter number1: "))):
    for j in range(i+1):
        print('*',end=" ")
    print()


# Enter number1: 5

## *
## * *
## * * *
## * * * *
## * * * * *


for i in range(1,(int(input("Enter number2: "))+1)):
    print()
    for j in range(1,i+1):
        print(j,end=" ")

# Enter number2: 5

## 1
## 1 2
## 1 2 3
## 1 2 3 4
## 1 2 3 4 5


for i in range(1,(int(input("Enter number3: "))+1)):
    print()
    for j in range(1,i+1):
        print(i,end=" ")

# Enter number3: 5

## 1
## 2 2
## 3 3 3
## 4 4 4 4
## 5 5 5 5 5