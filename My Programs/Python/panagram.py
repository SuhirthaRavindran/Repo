# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:10:55 2019

@author: admin
"""

#panagram contains all 26 alphabets(not case sensitive)
import string
#string.ascii_letters     [import string]               chr(97)='a'
#string.ascii_uppercase   [import string]               ord('A')=65
m=[]
stri=input("Enter: ")
stri=stri.lower() # NOT CASE SENSITIVE
for i in range(0,len(stri)):
    m.append(stri[i])
#print('m',m)
l1=[]    
l=string.ascii_lowercase
for i in range(0,len(l)):
    l1.append(l[i])
c=0  #Checks the condition for each word even if we remove i irrespective of its size, thus 'c' is important
#print('l1',l1)
while c!=len(stri):
    for i in l1:
        if i in m:
            l1.remove(i)
    c=c+1
#print('list =',l1)
if l1==[]:
    print("YES")
else:
    print("NO")



# abcdefghijKLMNOPqrstUVWxyZ

## YES