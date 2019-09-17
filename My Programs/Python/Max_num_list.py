# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:47:17 2019

@author: admin
"""

def isAlpha(char):
  return (char>='a' and char<='z') or (char<='A' and char>='Z')
l=[];m=[]                                       
string=input()  
count1=0                                                                      
for value in string:
  count=0
  if isAlpha(value)!=True:
    if value in'0123456789': # we can also use value.isdigit()
      count+=1
      if count>0:
        m.append(value)
        count1+=1
  a=len(m)
  if isAlpha(value)==True:
    sum=0
    for i in m:
      sum=sum+(int(i)*(10**(a-1)))
      a-=1
      m=[]
    if sum!=0:
      l.append(sum)
if m!=[]:
  a=len(m)
  num=0
  for i in m:
    num+=int(i)*(10**(a-1))
    a-=1
  if num!=0:
      l.append(num)
if l==[]:
  print(0)
else:
  print(max(l))
  
  
  
# abc156dda56fsf2s

## 156