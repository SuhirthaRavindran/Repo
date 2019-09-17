# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:59:17 2019

@author: admin
"""

###################              METHOD 1             #########################

matrix=[]
row=int(input("Enter row: "))
column=int(input("Enter column: "))
for i in range(row):
    l=[]
    for j in range(column):
        l.append(int(input("Enter value: ")))
    matrix.append(l)
for i in range(row):
    for j in range(column):
        print(matrix[i][j],end=" ")
    print()#\n
    
    
"""The output will be
       Enter row: 2
       Enter column: 2
       Enter value: 1
       Enter value: 2
       Enter value: 3
       Enter value: 4
       
       1 2
       3 4
"""

####################               METHOD 2            ########################

# We can also use this method:
l=[[0 for i in range(3)]for j in range(3)]
    #Output:
        #[[0,0,0],[0,0,0],[0,0,0]]


####################               METHOD 3           #########################

n=int(input())
l=[]
for i in range(n):
    l.append(input().split( ))
print(l)

"""
INPUT format:
    n = size of nxn matrix
    if n is 3,
    00 01 02
    10 11 12
    20 21 22

# The Output will be:
    [[00,01,02],[10,11,12],[20,21,22]]
"""