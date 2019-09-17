# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:38:30 2018

@author: admin
"""

a=input("Enter the character ")  # Do not use space while giving input
if (a=="a" or a=="e" or a=="i" or a=="o" or a=="i" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U"):
    print("Vowel")              # We can also use if a in 'aeiouAEIOU': print("Vowel")
else:
    print("Not a vowel")