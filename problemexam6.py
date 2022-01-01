# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:08:13 2021

@author: saira

"""

PhoneNoLetters = input("Enter a 10-character phone # in format XXX-XXXXXXX: ")

#replace the last 7 alphabetic characters by equivalent digits 

PhoneKeyCodes = {
    '1' : "1",
    'ABC' : '2',
    'DEF' : '3',
    'GHI' : '4',
    'JKL' : '5',
    "MNO" : '6',
    'PQRS' : '7',
    'TUV' : '8',
    'WXYZ' : '9',
    '+' : '0',
    '*' : '*error',
    '#' : '#ERROR'
     }




if len(PhoneNoLetters) != len("XXX-XXXXXXX"):
    print(PhoneNoLetters, "has {:d} letters & is not an expected phone #".
          format(len(PhoneNoLetters)))
else:
    PhoneNoStr = PhoneNoLetters[:4]
    for EachChr in PhoneNoLetters[4:]:
        for EachKey in PhoneKeyCodes.keys():
            if EachChr in EachKey and len(PhoneNoStr) < 12:
                PhoneNoStr += PhoneKeyCodes[EachKey]
                if len(PhoneNoStr) == 7:
                    PhoneNoStr += '-'
    print('{:s} is equivalent to {:s}'.format(PhoneNoLetters, PhoneNoStr))