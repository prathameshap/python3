#!/usr/bin/env python3

import math

class FindFibonacci:

    def __init__(self):
        self.val = False

    def isPerfectSquare(self, num:int)->bool:
        #import math

        s = int(math.sqrt(num))
        return s*s == num

    def isFibonacci(self, num:int)->bool:
        return self.isPerfectSquare(5*num*num+4) or self.isPerfectSquare(5*num*num-4)

    def fibonacciSimpleSum(self, n:int)->bool:

        for i in range(n):
            if (self.isFibonacci(i) == True) and (self.isFibonacci(n-i) == True):
                self.val = True
                    
        return self.val


        

        


