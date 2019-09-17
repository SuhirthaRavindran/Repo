# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:48:13 2019

@author: admin
"""

def down():
    for i in range(k,n-1):
        print(a[i][k],end=" ")
def right():
    for i in range(k,n-1):
        print(a[n-1][i],end=" ")
def up():
    i=n-1
    while i>=0:
        if i>=k:
            print(a[i][n-1],end=" ")
            i-=1
        else:
            break
def left():
    for i in range(n-2,k,-1):
        print(a[k][i],end=" ")
n=int(input())
a=[]
for i in range(n):
  l=input().split( )
  a.append(l)
k=0
h=n+n+1
while True:
    if h==0:
        break
    down()
    h-=1
    if h==0:
        break
    right()
    h-=1
    if h==0:
        break
    up()
    h-=1
    if h==0:
        break
    left()
    h-=1
    k+=1
    n-=1




# 3
# 1 2 3
# 4 5 6
# 7 8 9

## 1 4 7 8 9 6 3 2 5