#m=int(input())
#n=int(input())
#a=[]
##for i in range(m):
    ##a.append([int(j) for j in range(n)])
    ##for j in range(n):
    ##a.append([int(input()) for j in range(n)])
#for l in range(1,((m*n)+1)):#
#    a.append([int(l) for j in range(n)])#
#print(a)
##n = int(input()) 
##a = []
##for i in range(n):
##   a.append([int(j) for j in input().split()])
##print(a)



   ###SORTING USING RANDOM LIBRARY### 
from random import randint
n=int(input())
list_1=[]
flag=0
for i in range(n):
  list_1.append(int(input()))
while flag!=1:
    m=randint(0,n-1)
    o=randint(0,n-1)
    list_1[m],list_1[o]=list_1[o],list_1[m]
    for j in range(n-1):
        if list_1[j]>list_1[j+1]:
            flag=0
            break
        else:
            flag=1 
for i in list_1:
  print(i)



# 3

# 1
# 3
# 2

## 1
## 2
## 3

"""
         OR

lines 36 and 37 can be

"""
s=[str(k) for k in list_1]
print(' '.join(s))

#THIS PRINTS THE OUTPUT ELEMENTS WITH SPACE IN BETWEEN THEM AND WITHOUT SPACE AT THE END

'''Eg,1(space)2(space)3(no space),that is,1 2 3'''


# 3

# 3
# 1
# 2

## 1 2 3