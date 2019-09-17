# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:10:55 2019

@author: admin
"""

#input - list
n=int(input())
l=[]
for i in range(n):
    a=input().split( )
    l.append(a)

#Actual process for upper triangular matrix
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            if i==j:
                if (j-k)<0:
                    continue
                l[i][j-k]=0
            else:
                break
print(l)  #Printing matrix method:1


# 3
# 1 2 3
# 4 5 6
# 7 8 9

## [['1','2','3'],[0,'5','6'],[0,0,'2']]
'''
[printing matrix method:2]
for i in range(n):
    if i>=0:
        for j in range(n):
            if j>=0:
                if j==n-1:                       Output will be in the format:
                    print(l[i][j],sep="\n")         00  01
                    if i==n-1:                      10  11
                        continue
                else:
                    print(l[i][j],end=" ")
'''

# 3
# 1 2 3
# 4 5 6
# 7 8 9

## 1 2 3
## 0 5 6
## 0 0 9

'''
00    01    02
10    11    12      #Example of indexing in matrix
20    21    22
'''