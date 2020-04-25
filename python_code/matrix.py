#!/usr/bin/env python3

#############################################################################################
##  Matrix Class -  supporting meathods
##                  initialize - given row and columns
##                  insert     - insert at given index
##                  addScaler  - add given scaler value to the matrix
##                  mulScaler  - multiply given scaler value with the matrix
##                  printMtx   - print given matrix
#############################################################################################

class Matrix:
    
    """Creates object of  class Matrix with number of rows and columns"""
    def __init__(self, *args):
        
        numargs = len(args)

        if numargs < 1:
            raise TypeError(f'Epected at least one argument, got {numargs}')
        elif numargs == 1:
            print(f'Created square matrix {numargs}x{numarags}')
            self._rows    = args[0]
            self._columns = args[0]
        elif numargs == 2:
            self._rows    = args[0]
            self._columns = args[1]
        else:
            raise TypeError(f'At most 2 arguments ara permitted, but got{numargs}')
        self.initMatrix(0)
            
    """Initializes matrix with given int val and return int list of list"""
    def initMatrix(self, val:int)->int:
        self._matrix = [[val for x in range(self._columns)] for y in range(self._rows)]
        return self._matrix

    """Changes the value of perticular position in matrix"""

    def changeElements(self, **kwargs):
        rw_chng  = None
        cl_chng  = None
        val_chng = None
        
        if 'row' in kwargs:
            rw_chng = kwargs['row']
            if rw_chng != None and rw_chng > self._rows: raise IndexError(f'Row number exceeded beyond matrix bounds')
        if 'col' in kwargs:
            cl_chng = kwargs['col']
            if cl_chng != None and cl_chng > self._columns: raise IndexError(f'Column number exceed beyond matrix bounds')
        if 'val' in kwargs: val_chng = kwargs['val']

        if val_chng  == None: raise TypeError(f'Missing value parameter')
        elif rw_chng == None and cl_chng == None: raise TypeError(f'At least a row or column value required')
        else: print(f'Resultant Matrix')

        if rw_chng == None:
            for i in range(self._rows):
                self._matrix[i][cl_chng-1] = val_chng
        elif cl_chng == None:
            for i in range(self._columns):
                self._matrix[rw_chng-1][i] = val_chng
        else:
            self._matrix[rw_chng-1][cl_chng-1] = val_chng

        return self._matrix

    """Multiply matrix by a scaler value"""

    def scalerMultiplier(self, scal_val):

        if scal_val != None:

            for i in range(self._rows):
                for j in range(self._columns):
                    self._matrix[i][j] *= scal_val

            return self._matrix
        else:
            raise TypeError(f'Need scaler value to multiply')

    """Add perticular scaler value to matrix"""

    def scalerAddition(self, scal_val):

        if scal_val != None and scal_val != 0:

            for i in range(self._rows):
                for j in range(self._columns):
                    self._matrix[i][j] += scal_val

            return self._matrix
        elif scal_val == 0:
            return self._matrix
        else:
            raise TypeError(f'Need scaler value to Add')

    """Print the resulting Matrix"""

    def printMatrix(self):
        for row in self._matrix:
            print(row)

    """Finding Transpose of the matrix"""

    def findTranspose(self):

        tr_matrix = [[self._matrix[j][i] for j in range(len(self._matrix))]for i in range(len(self._matrix[0]))]

        print(f'Transpose is')

        for row in tr_matrix:
            print(row)
