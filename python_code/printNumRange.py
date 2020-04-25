#!/usr/bin/env python3


#print1toN.py  auther prathamesh pawar

"""In this file we are asking for input from user 
for 3 things starting number, ending number and 
step value for the step increament to print the 
numbers"""

class PrintNumberRange:
    
    #printing list using for and in range functio
    def print1ToNUsingFor(self, *args:int)->int:
        numargs = len(args)
        start = 0
        step  = 1
        self.lst = []
        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            stop = args[0]
        elif numargs == 2:
            start = args[0]
            stop  = args[1]
        elif numargs == 3:
            start = args[0]
            stop  = args[1]
            step  = args[2]
        else:
            raise TypeError(f'expected maximum 3 arguments, got {numargs}')
        
        #populating the list
        
        for i in range(start, stop, step):
            self.lst.append(i)

        return self.lst

    #printing the list using while loop
    def print1ToNUsingWhile(self, *args:int)->int:
        numargs = len(args)
        start = 0
        step  = 1
        self.lst = []

        if numargs < 1:
            raise TypeError('atleast 1 argument is required, got {numarags}')
        elif numargs == 1:
            stop = args
        elif numargs == 2:
            start = args[0]
            stop  = args[1]
        elif numargs == 3:
            start = args[0]
            stop  = args[1]
            step  = args[2]
        else:
            raise TypeError ('maximum 3 arguments are acceptable, got {numargs}')
        
        #populating the list
        while start < stop:
            self.lst.append(start)
            start += step

        return self.lst

    def print1ToNnumbers(self, *args: int)->int:
        numargs = len(args)
        start = 0
        step  = 1
        self.lst = []

        if numargs < 1:
    
    #Problem - Is it possible to use for without using range..??
