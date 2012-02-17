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
    >>> i2.total()
    3.98

"""

class Ammount(object):

    def __init__(self, attr):
        self.attr = attr        

    def __get__(self, obj, obj_type=None):
        """Ammount of items in the Order"""
        return getattr(obj, self.attr)

    def __set__(self, obj, value):
        if value < 1:
            raise ValueError("amt must be one or higher")
        else:
            setattr(obj, self.attr, value)


"""Class that defines an Item of a Order"""
class ItemOrder(object):
   
    def __init__(self, cod, amt, price, per_box=1):
        """Creates a new Item from an Order.

        cod - Code of the item
        amt - Ammount of items
        price - Price of the item
        per_box - How many items fill a full box

        >>> i = ItemOrder('ABC123', 1, 0.99)        

        """        
        self._cod = cod
        self._amt = amt
        self._price = price
        self._per_box = per_box
        
    amt = Ammount('_amt')
    per_box = Ammount('_per_box')


    def total(self):
        """Gets the total of items times price"""
        return self._amt * self._price
    
if __name__ == '__main__':
    i = ItemOrder('ABC123', 1, 0.99)
    i2 = ItemOrder('ABC124', 2, 1.99, 6)
