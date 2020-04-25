#!/usr/bin/env python3

"""This class takes a number and gives back matrix containing square
root of the number.  i.e. if user inputs 16 then we will get back 
matrix of size 4x4 and all of it's elements will be 4"""

class MatrixOfSqrts:

    

    def matrixOfSqrt(self, num:int)->int:
        import math
        nm    = num
        start = 0
        end   = 0
        self.matrix = []

        #check if the number is perfect square

        sq  = math.sqrt(nm)
        if(sq - math.floor(sq))!=0:
            raise TypeError('expected perfect square but got {nm}')
        else:
            sq = int(sq)
            end += sq
            #self.matrix=[[ sq for i in range(sq)]for j in range(sq)]
            for i in range(sq):
                self.matrix.append([ j for j in range(start, end)])
                start += sq
                end += sq

                    

        return self.matrix
