# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:25:03 2021

@author: saira

"""

print("input 5 birthdays from 5 users (1 each)")
BirthDays = {}
Count = 0
for iBday in range(5):
    BDayMonthNum = input("Enter birthday as 'Month #': ")
    SplitBDayMonthNum = BDayMonthNum.strip("\n").split(' ')
    BirthMonth = SplitBDayMonthNum[0]
    BirthDay = int(SplitBDayMonthNum[1])
    if BirthMonth in BirthDays: # repeat (month(s))
        Count += 1
        BirthDays[BirthMonth + str(Count)] = BirthDay
    else:
        BirthDays[BirthMonth] = BirthDay

# calender-ordered months to check chronological order
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# put in chronological order
SortedBDays = []
for Month in Months:
    for EachMonth in BirthDays: #.keys():
        if EachMonth == Month:
            SortedBDays += [EachMonth + ' ' + str(BirthDays[EachMonth])]
        else: # repeat month(s)
            for nRepeat in range(1, Count + 1):
                if EachMonth == Month + str(nRepeat):
                    ActualMonth = EachMonth.strip(str(nRepeat))
                    if BirthDays[EachMonth] < BirthDays[ActualMonth]:
                        SortedBDays.insert(-1, ActualMonth + ' ' + str(BirthDays[EachMonth]))
                        # make sure in order for 2 but >2?
                    else:
                        SortedBDays += [ActualMonth + ' ' + str(BirthDays[EachMonth])]

print("Sorted birthdays:\n", SortedBDays) # output however you like