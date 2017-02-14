
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
        print "PLAY"
        for hand in self.hands:
            print "Playing Hand: %s" % hand
            self.play_hand(hand, shoe)

    def play_hand(self, hand, shoe):
        if hand.length() < 2:
            if hand.cards[0].name == "Ace":
                hand.cards[0].value = 11
            self.hit(hand, shoe)

        not_busted = not hand.busted()
        not_bj = not hand.blackjack()
        not_surrender = not hand.surrender
        break_now = False

        while not_busted and not_bj and not_surrender:
            flag = self.strategy.select_action(self, hand)
            print "Playing: %s" % hand
            print "Response: %s" % flag

            if flag == 'D':
                if hand.length() == 2:
                    print "Double Down"
                    hand.doubled = True
                    self.hit(hand, shoe)
                    break_now = True
                else:
                    print "Hitting (but picked Double)"
                    flag = 'H'

            if flag == 'Sr':
                if hand.length() == 2:
                    print "Surrender"
                    hand.surrender = True
                    break_now = True
                else:
                    print "Hit (but picked Surrender)"
                    flag = 'H'

            if flag == 'H':
                print "Hit"
                self.hit(hand, shoe)

            if flag == 'P':
                print "Split"
                self.split(hand, shoe)

            if flag == 'S':
                break_now = True
                print "Stand"

            not_busted = not hand.busted()
            not_bj = not hand.blackjack()
            not_surrender = not hand.surrender

            print "Recording in-hand result:"
            self.strategy.record_result(hand, self)

            if break_now:
                break

        print "Finishing Play.."

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


