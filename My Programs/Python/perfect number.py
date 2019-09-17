# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:05:04 2018

@author: admin
"""

n=int(input("Enter the value of n"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print("Perfect number")
else:
    print("Not a Perfect number\a") #\a for bell rings