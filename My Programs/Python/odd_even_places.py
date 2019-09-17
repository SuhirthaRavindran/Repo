# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:48:12 2019

@author: admin
"""

# " within these ("") quotes are replaced by n=list(str(n)) "
"""def modify(n): #modify(n,count)
    l=[]
    while n!=0:
        r=n%10
        '''count=count+1
        if count%2==0:
            l.append(r)'''
        #
        l.append(r)
        n=n//10
    return l # Here l is reversed modified list"""
n=int(input())
#n=list(str(n))    ######## if this line is here it shows error for line 35 and 38
'''if n%2==0:
    count=0
    l=modify(n,count)
else:
    count=1
    l=modify(n,count)'''
#
"""l=modify(n)"""
#
m=[]
"""for i in range(len(l)-1,-1,-1):  # This for loop is for making the reversed modified list in proper order
    l.append(l[i])
    l.pop(i)"""
if n%2==0:
    n=list(str(n))# Or use:- if int(n[len(n)-1])%2==0 in line 35 and write this line for ONE time in line 21 alone
    for i in range(0,len(n),2):
        m.append(int(n[i]))# Instead of int(n[i]) use:- ""n=list(map(int,n))"" after ''n=list(str(n))
else:
    n=list(str(n))
    for i in range(1,len(n),2):
        m.append(int(n[i]))
for i in range(len(m)):  # This for loop is for printing a number say 9 as 9 instead of 09 or 009
    if m[i]!=0:
        m=m[i:]
        break
for i in m:
    print(i,end="")



# 245872    # 1009

## 257     ## 9

# Explanation:
    # 245872 is EVEN number
    # 1 2 3 4 5 6                  ''' 5 4 3 2 1 0 '''
    # 2 4 5 8 7 2
    # So numbers in even (2,4,6) places are removed  ''' (0,2,4) '''
    ## 257
    
    # Similarly, 1009 is ODD number  ''' 3 2 1 0 '''
    # 1 2 3 4
    # 1 0 0 9
    # So numbers in odd (1,3) places are removed  ''' (1,3) '''
    ## 09 => 9