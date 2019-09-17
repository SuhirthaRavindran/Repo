# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:12:08 2019

@author: admin
"""

import string
l=input()
count=0
for i in l:
    if i in string.ascii_letters:
        print(i,end="")
        count=0
    elif i==" ":               # Do not use "\t"
        count=count+1
        if count>1:
            print("*",end="")
        else:
            print(" ",end="")  # Do not use "\t"
    else:
        print(i,end="")        # For Special characters and numbers
        count=0




# She sells    sea  shells on    the       sea shore

## She sells ***sea *shells on ***the ******sea shore