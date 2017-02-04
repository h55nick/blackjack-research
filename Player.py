
class Player(object):
    """
    Represent a player
    """
    def __init__(self, hand=None, dealer_hand=None, strategy=None):
        self.strategy = strategy
        self.hands = [hand]
        self.dealer_hand = dealer_hand

    def set_hands(self, new_hand, new_dealer_hand):
        self.hands = [new_hand]
        self.dealer_hand = new_dealer_hand

    def play(self, shoe):
        for hand in self.hands:
            print "Playing Hand: %s" % hand
            self.play_hand(hand, shoe)

    def play_hand(self, hand, shoe):
        if hand.length() < 2:
            if hand.cards[0].name == "Ace":
                hand.cards[0].value = 11
            self.hit(hand, shoe)

        while not hand.busted() and not hand.blackjack() and not hand.surrender:
            flag = self.strategy.select_action(self, hand)
            print "Playing: %s" % hand
            print "Response: %s" % flag

            if flag == 'D':
                if hand.length() == 2:
                    print "Double Down"
                    hand.doubled = True
                    self.hit(hand, shoe)
                    break
                else:
                    flag = 'H'

            if flag == 'Sr':
                if hand.length() == 2:
                    print "Surrender"
                    hand.surrender = True
                    break
                else:
                    flag = 'H'

            if flag == 'H':
                self.hit(hand, shoe)

            if flag == 'P':
                self.split(hand, shoe)

            if flag == 'S':
                break

    def hit(self, hand, shoe):
        c = shoe.deal()
        hand.add_card(c)
        print "Hitted: %s" % c

    def split(self, hand, shoe):
        if hand.splitable():
            self.hands.append(hand.split())
            print "Splitted %s" % hand
            self.play_hand(hand, shoe)
        else:
            print "Can't split this hand"


