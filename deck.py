# encoding: utf-8

"""Represents a standard card for a Deck. A standard card is defined by two 
attributes, usually a value and a suit::

    >>> zape = StandardCard('4','♣')
    >>> zape
    <4♣>

"""
class StandardCard(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '<%s%s>' % (self.value, self.suit)

    def __str__(self):
        return self.value+self.suit
        
"""
Represents a Card from the game Super Trunfo.::

"""        
class SuperTrunfoCard(StandardCard):

    def __init__(self, name, value, suit, chars=None):
        StandardCard.__init__(self, value, suit)
        self.name = name
        if chars is None:
            self.chars = {}
        else:
            self.chars = chars

    def __repr__(self):
        return '<Trunfo:%s,%s%s>' % (self.name, self.value, self.suit)
    
        
"""Represents a complete (generic) deck, a collection of Cards (any item)."""        
class Deck(object):

    def __init__(self):
        self.__cards = []

    def __len__(self):
        """Number of Cards in the Deck."""
        return len(self.__cards)
        
    def __iter__(self):
        """Gets a simple Deck iterator, going from first to last card."""
        for c in self.__cards:
            yield c

    def __getitem__(self, pos):
        """Get a Card from the Deck."""
        return self.__cards[pos]

    def __setitem__(self, pos, card):
        """Set a card in a specific position of the Deck."""
        self.__cards[pos] = card
    
    def __repr__(self):
        """Returns the string repr() of the list of card."""
        return repr(self.__cards)

    def __str__(self): 
        """Returns the string representation of all cards of the deck."""
        return ' '.join([str(c) for c in self.__cards])

    def append(self, item):
        """Append a card or deck to the deck.::
        
           item - card or deck to be appended to the end of the deck
        """
        self.__cards.extend(item)

    def draw(self, pos=0):
        """Draws a card from the deck from the deck, removing it. Returns None
           if the deck is empty.::

           pos - Position of the card, 0 (top) by default
        """
        if len(self.__cards) == 0:
            return None
        else:
            c = self.__cards[pos]
            del self.__cards[pos]
            return c
            
    def shuffle(self):
        """Shuffle the deck of cards, modifying the list."""
        from random import shuffle
        shuffle(self.__cards)

class BasicDeckIterator(object):

    def __init__(self, deck):
        self.__deck = deck
        self.__pos = 0
        
    def next(self):
        return (c for c in self.__deck._Deck__cards)
        
    def __iter__(self):
        return self
    
    __next__ = next # For Python 3.0+
    
class ReversedDeckIterator(object):

    def __init__(self, deck):
        self.__deck = deck
        self.__pos = len(self.__deck) - 1
        
    # Alternative to next method:
    # return (i for i in reversed(self.__deck._Deck__cards))
    def next(self):
        if self.__pos == -1:
            raise StopIteration()
        c = self.__deck._Deck__cards[self.__pos]  # Just not to use __getitem__
        self.__pos -= 1
        return c
        
    def __iter__(self):
        return self
    
    __next__ = next # For Python 3.0+
        

class StandardDeck(Deck):
    """Represents a complete (standard) deck::

        >>> d = StandardDeck()
        >>> len(d)
        52
        >>> d[0]
        <A♠>
        >>> print d
        A♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠ A♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥ A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣ A♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦
        >>> for c in d: print c
        ... 
        A♠
        2♠
        3♠
        4♠
        5♠
        6♠
        7♠
        8♠
        9♠
        10♠
        J♠
        Q♠
        K♠
        A♥
        2♥
        3♥
        4♥
        5♥
        6♥
        7♥
        8♥
        9♥
        10♥
        J♥
        Q♥
        K♥
        A♣
        2♣
        3♣
        4♣
        5♣
        6♣
        7♣
        8♣
        9♣
        10♣
        J♣
        Q♣
        K♣
        A♦
        2♦
        3♦
        4♦
        5♦
        6♦
        7♦
        8♦
        9♦
        10♦
        J♦
        Q♦
        K♦
        >>> [c for c in reversed(d)][:3]
        [<K♦>, <Q♦>, <J♦>]
        >>> d[0], d[1] = d[1], d[0]
        >>> print d[0:3]
        [<2♠>, <A♠>, <3♠>]
        >>> print d.draw()
        2♠
        >>> len(d)
        51

    """

    values = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    suit = '♠ ♥ ♣ ♦'.split()

    def __init__(self):
        Deck.__init__(self)
        cards = [StandardCard(s, v)
                   for v in self.suit
                   for s in self.values]
        self.append(cards)
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()    
    d = Deck()
    s = StandardDeck()
