# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:26:31 2021

@author: saira

"""
# problem 41

def isProperDivisor(Int, eachInt):
    ProperDiv = False
    # takes in two numbers and test whether they have a remainder or not
    for eachInt in range(Int):
        if Int % eachInt:
            ProperDiv = False
        else:
            ProperDiv = True
        return ProperDiv
# test 
print(isProperDivisor(2,1))

def GetDivisors(AnInt):
    Divisors = []
    for EachInt in range(1, AnInt):
        if isProperDivisor(AnInt, EachInt):
            Divisors += [EachInt]
    return Divisors
# test
print(GetDivisors(6))

def isPerfectNum(CanInt):
    if sum(GetDivisors(CanInt)) == CanInt:
        return True
    else:
        return False
    
# test       
print(isPerfectNum(6))