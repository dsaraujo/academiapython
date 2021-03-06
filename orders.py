# coding: utf-8

"""
Generic Doc Tests

    >>> i = ItemOrder('ABC123', 1, 1.99)
    >>> i2 = ItemOrder('ABC124', 2, 1.99, 6)
    >>> i.amt
    1
    >>> i.amt = 2
    >>> i.amt = -3
    Traceback (most recent call last):
        ...
    ValueError: amt must be one or higher
    >>> i.amt
    2
    >>> i.total()
    3.98

"""

"""Class that defines an Item of a Order"""
class ItemOrder(object):
    
    def __init__(self, cod, amt, price, per_box=1):
        """Creates a new Item from an Order.

        cod - Code of the item
        amt - Ammount of items
        price - Price of the item

        >>> i = ItemOrder('ABC123', 1, 0.99)        

        """        
        self.__cod = cod
        self.__amt = amt
        self.__price = price
        self.__per_box = per_box

    @property
    def amt(self):
        """Ammount of items in the Order"""
        return self.__amt

    @amt.setter
    def amt(self, value):
        if value < 1:
            raise ValueError("amt must be one or higher")
        else:
            self.__amt = value

    def total(self):
        """Gets the total of items times price"""
        return self.__amt * self.__price
    
if __name__ == '__main__':
    i = ItemOrder('ABC123', 1, 0.99)
    i2 = ItemOrder('ABC124', 2, 1.99, 6)
