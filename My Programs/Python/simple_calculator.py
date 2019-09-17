# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:21:08 2018

@author: admin
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):                             # we can also write:  return a//b,a%b
    print(a,"/",b,"=",a//b)
    print("The remainder of",a,"and",b,"is",a%b)
print("select operator")                  # we can also use triple quotes '''
print("1.Addition")                       # print(''' 1. Addition
print("2.Subtraction")                           #    2.Subtraction
print("3.Multiplication")                        #    3.Multiplication
print("4.Division")                              #    4.Division''')
n=int(input("Enter your choice number : "))
number1=int(input("Enter the first number : "))
number2=int(input("Enter the second number : "))
if n==1:
    print(number1,"+",number2,"=",add(number1,number2))
elif n==2:
    print(number1,"-",number2,"=",sub(number1,number2))
elif n==3:
    print(number1,"*",number2,"=",mul(number1,number2))
elif n==4:
    div(number1,number2)
else:
    print("Choose number between 1 and 4 only")