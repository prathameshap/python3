#!/usr/bin/env python3


def printNumWhile(n:int):
    if n == 0:
        return
    else:
        printNumWhile(n-1)
        print(n)

    

    
    
"""
def printRecursiveHelper(target: int, cVal: int):
    if cVal > target:
        return
    else:
        print(cVal)
        printRecursiveHelper(target, cVal + 1)
"""

