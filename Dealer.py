class Dealer(object):
    """
    Represent the dealer
    """
    def __init__(self, hand=None):
        self.hand = hand

    def set_hand(self, new_hand):
        self.hand = new_hand

    def play(self, shoe):
        while self.hand.value < 17:
            self.hit(shoe)

    def hit(self, shoe):
        c = shoe.deal()
        self.hand.add_card(c)
        print "Dealer hitted: %s" %c

