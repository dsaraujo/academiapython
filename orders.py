# coding: utf-8

"""
Generic Doc Tests

    >>> i = ItemOrder('ABC123', 1, 0.99)
    >>> i.amt
    1
    >>> i.amt = -3
    Traceback (most recent call last)
        ...
    Value Error: ammount must be positive
    >>> i.amt
    1

"""

"""Class that defines an Item of a Order"""
class ItemOrder(object):
    
    def __init__(self, cod, amt, price):
        """Creates a new Item from an Order.

        cod - Code of the item
        amt - Ammount of items
        price - Price of the item

        >>> i = ItemOrder('ABC123', 1, 0.99)        

        """        
        self._cod = cod
        self._amt = amt
        self._price = price

        
    
