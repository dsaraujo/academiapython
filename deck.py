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
Represents a Card from the game Super Trunfo::
    
    >>> s = SuperTrunfoCard('Ferrari', 10, {'velocidade':20})
    >>> s
    <Trunfo:Ferrari,(10, {'velocidade': 20})>

"""        
class SuperTrunfoCard(object):

    def __init__(self, name, *attr):
        self.name = name
        self.attr = attr

    def __repr__(self):
        return '<Trunfo:%s,%s>' % (self.name, self.attr)
    
        
"""Represents a complete (generic) deck, a collection of Cards (any item)"""        
class Deck(object):

    def __init__(self):
        self.__cards = []

    def __len__(self):
        """Number of Cards in the Deck"""
        return len(self.__cards)

    def __getitem__(self, pos):
        """Get a Card from the Deck"""
        return self.__cards[pos]

    def __setitem__(self, pos, card):
        """Set a card in a specific position of the Deck"""
        self.__cards[pos] = card

    def __repr__(self):
        """Returns the string repr() of the list of card"""
        return repr(self.__cards)

    def __str__(self): 
        """Returns the string representation of all cards of the deck"""
        return ' '.join([str(c) for c in self.__cards])

    def append(self, item):
        """Append a card or deck to the deck
        
           item - card or deck to be appended to the end of the deck
        """
        self.__cards.extend(item)

    def draw(self, pos=0):
        """Draws a card from the deck from the deck, removing it. Returns None
           if the deck is empty::

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


class StandardDeck(Deck):
    """Represents a complete (standard) deck::

        >>> d = StandardDeck()
        >>> len(d)
        52
        >>> d[0]
        <A♠>
        >>> print d
        A♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠ A♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥ A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣ A♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦
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
