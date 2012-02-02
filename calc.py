# coding: utf-8
# Simulates an extensible calculator (now using OO)
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
        self.ops = Calculator.standard_ops
        self.currentop = self.ops['+']
        self.total = 0
    
    def processLine(self, line):
        """Process the line and returns a message (can be empty)"""
        if line == '\x1b':                          # \x1b =>  Esc
            self.currentop = self.ops['+']
            self.total = 0
            return 'Clr'
        elif self.ops.has_key(line):
            self.currentop = self.ops[line]
        else:
            err = ''
            try:
                f = float(line)
                self.total = self.currentop(self.total, f)
            except ValueError:
                err = 'Err: %s' % line
            return err
    
    def addOp(self, key, func):
        # TODO: Test if func can only receives 2 floats arguments and
        #       returns a float, otherwise throws an Exception
        self.ops[key] = func
    
    def getOp(self):
        """Return the string of the current operation, empty string if not found"""
        for k in self.ops.keys():
            if self.ops[k] is self.currentop:
				return k
        return ''


if __name__ == "__main__":
    
    def lessPercent(a,b):
        """Reduces the value a in b%. Returns the reduced value.
        Ex: lessPercent(100, 10) returns 100-10%, 90."""
        return a-(a*(b/100))
    
    def plusPercent(a,b):
        """Increases the value a in b%. Returns the reduced value.
        Ex: lessPercent(100, 10) returns 100+10%, 110."""
        return a+(a*(b/100))
    
    c = Calculator()   # Instantiate a new calculator
    c.addOp('-%', lessPercent)  # Customize it with additional operations
    c.addOp('+%', plusPercent)
    
    while True:
        print c.total
        p = raw_input(c.getOp())
        if not p.strip(): break
        out = c.processLine(p)
        if out: print out 
