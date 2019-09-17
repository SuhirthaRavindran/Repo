# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:23:52 2019

@author: admin
"""

s=input().split( )
c=0
for i in range(len(s)):
    s[0]=s[i].split(':')
    if int(s[0][0])==10 and int(s[0][1])>0 or int(s[0][0])>10:
        c+=1
print("Number of late comers are:",c)

##########  Prints number of latecomers who arrive after 10:00 a.m  ###########


# 10:00 10:01 11:00 10:20 09:50 08:55

## Number of late comers are: 3