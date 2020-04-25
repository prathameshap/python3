#!/usr/bin/env python3


class MatchPattern:

    def __init__(self):
        self.zero = ['a','e','i','o','u', 'y']


    def findMatch(self, pattern:str, s:str)->int:

        string  = ""

        for _ in s: 
            if _ in self.zero:
                string += '0'
            else:
                string += '1'

        print(string)

        res = string.count(pattern)

        return res
