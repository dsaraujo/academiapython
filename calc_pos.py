# coding: utf-8
# Simulates an extensible calculator (now using O.O.)
__author__ = 'Daniel Araujo'

import operator as op

class Calculator(object):
    
    standard_ops = { # Default operations
    '+':op.add,
    '-':op.sub,
    '*':op.mul,
    '/':op.div,
    '**':op.pow
    }
    
    def __init__(self):
        self.ops = Calculator.standard_ops.copy()   # Copy from class
    
    def stepList(self, l):
        if len(l) <= 1:
            return l
        last = l[-1]
        if str(last).isdigit(): # Empilhamento
            return l
        else: # Operação
            if len(l) < 3: raise TypeError('Need at least 2 operands to do '+last)
            prelist = []
            if len(l) > 3:
                prelist = l[:-3]
            prelist.append(self.ops[l[-1]](l[-2], l[-3]))
            return prelist       

    # TODO: Tratar mais de uma operação. Só trata uma por lista.   
    
    def addOp(self, key, func):
        # TODO: Test if func can only receives 2 floats arguments and
        #       returns a float, otherwise throws an Exception
        self.ops[key] = func
    
    def getOp(self):
        """Return the string of the current operation, 
        empty string if not found"""
        for k in self.ops.keys():
            if self.ops[k] is self.currentop:
				return k
        return ''


if __name__ == "__main__":
    
    
