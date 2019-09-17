# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:27:07 2019

@author: admin
"""

s=list(input())
count=1
for i in range(len(s)):
    if not s[i].isalpha() and not s[i].isdigit():
        if count==0:
            s[i]=','
            count=1
        else:
            s[i]='.'
            count=0
for i in range(len(s)):
    print(s[i],end="")




#  a,hgjk.ksjk;ksjk[slk]d

## a.hgjk,ksjk.ksjk,slk.d