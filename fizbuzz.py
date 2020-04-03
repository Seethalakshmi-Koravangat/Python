# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:07:49 2020

@author: Unnikrishnan AR
"""

def fiz_buzz(input):
    if input%3 == 0 and input%5 == 0:
        return 'FIZZBUZZ'
    if input%3 == 0:
        return 'FIZZ'
    if input%5 == 0:
        return 'BUZZ'
    
    return input
        
        
print(fiz_buzz(15))