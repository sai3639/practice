# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:55:16 2021

@author: saira

"""

# input a person's age
inputAge = int(input("input a person's age (or -1 when done): "))

#continue to ask for input unitl negative # entered, indicating that user done inputting data

Rock0Ages = []

while inputAge > -1:
    Rock0Ages.append(inputAge)
    inputAge = int(input("input a person's age (or -1 when done): "))
    
    
#determine the total # of people and the minimum and maximum ages entered
print("   {:<16s}  {:<11s}  {:<11s}".format('Number of people', 'Minimum age', 'Maximum age'))
print("    {:<16d}  {:<11d}  {:<11d}".format(len(Rock0Ages), min(Rock0Ages), max(Rock0Ages)))