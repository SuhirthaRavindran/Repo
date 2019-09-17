# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:36:41 2019

@author: admin
"""

n=int(input())
l=[]
if n%2==0:
    while n!=0:
        r=n%10
        if r%2!=0:
            l.append(r)
        n=n//10
else:
    while n!=0:
        r=n%10
        if r%2==0:
            l.append(r)
        n=n//10
for i in range(len(l)-1,0,-1):
    print(l[i],end="")
print(l[0])




# 245872           # 154863

## 57             ## 486

# Explanation:
    # Here if number is even the odd digits are printed and vice versa