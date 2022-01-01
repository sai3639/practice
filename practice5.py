# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:29:57 2021

@author: saira

"""

# BellaWantsEg = int(input("WhatDoesBellaWant (0 or no)? "))
# HowManyTimesAsked = 0


# while BellaWantsEg:
#     print("An easy loop because BellaWantsEg", BellaWantsEg)
#     BellaWantsEg = int(input("WhatDoesBellaWant (0 or no)? "))
#     HowManyTimesAsked += 1
#     print("I had to ask {:d} times".format(HowManyTimesAsked))
    
    
Sum = 0
for i in range(10):
    Sum += i +1
print(Sum)


for i in range(10):
    for j in range(10):
        print(i, "times", j, "equals", i * j)


TotRows = 7
TotCols = 5

for EachRow in range(TotRows):
    for EachCol in range(TotCols):
        print("{:d}, {:d}".format(EachRow, EachCol).center(7), end= ' ')
    print()
    
    
    
    
    # table where each element is row count times column
for EachRow in range(1, 1 + TotRows):
    for EachCol in range(1, 1 + TotCols):
        print("{:d}".format(EachRow * EachCol).center(7), end= ' ')
    print()
        
# table where each element is row count squared times column #/count

for EachRow in range(1, 1 + TotRows):
    for EachCol in range(1, 1 + TotCols):
        print("{:d}".format((EachRow**2) * EachCol).center(7), end= ' ')
    print()