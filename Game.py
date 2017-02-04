from Dealer import Dealer
from Player import Player

from Hand import Hand
from Card import Card
from Shoe import Shoe

SHOE_SIZE = 6
class Game(object):
    """
    A sequence of Blackjack Rounds that keeps track of total money won or lost
    """
    def __init__(self, strategy=None):
        self.shoe = Shoe(SHOE_SIZE)
        self.money = 0.0
        self.bet = 0.0
        self.stake = 1.0
        self.player = Player(strategy=strategy)
        self.dealer = Dealer()

    def get_status(self, hand):
        if not hand.surrender:
            if hand.busted():
                status = "LOST"
            else:
                if hand.blackjack():
                    if self.dealer.hand.blackjack():
                        status = "PUSH"
                    else:
                        status = "WON 3:2"
                elif self.dealer.hand.busted():
                    status = "WON"
                elif self.dealer.hand.value < hand.value:
                    status = "WON"
                elif self.dealer.hand.value > hand.value:
                    status = "LOST"
                elif self.dealer.hand.value == hand.value:
                    if self.dealer.hand.blackjack():
                        status = "LOST"  # player's 21 vs dealers blackjack
                    else:
                        status = "PUSH"
        else:
            status = "SURRENDER"
        return status


    def get_hand_winnings(self, hand):
        win = 0.0
        bet = self.stake
        status = self.get_status(hand)

        if status == "LOST":
            win += -1
        elif status == "WON":
            win += 1
        elif status == "WON 3:2":
            win += 1.5
        elif status == "SURRENDER":
            win += -0.5
        if hand.doubled:
            win *= 2
            bet *= 2

        win *= self.stake

        return win, bet, status

    def play_round(self):
        self.stake = 1.0

        player_hand = Hand([self.shoe.deal(), self.shoe.deal()])
        dealer_hand = Hand([self.shoe.deal()])
        self.player.set_hands(player_hand, dealer_hand)
        self.dealer.set_hand(dealer_hand)
        print "Dealer Hand: %s" % self.dealer.hand
        print "Player Hand: %s\n" % self.player.hands[0]

        self.player.play(self.shoe)
        self.dealer.play(self.shoe)

        for hand in self.player.hands:
            win, bet, flag = self.get_hand_winnings(hand)
            self.money += win
            self.bet += bet

            self.player.strategy.record_result(win=win,status=flag, bet=bet, hand=hand)
            # print "Player Hand: %s %s (Value: %d, Busted: %r, BlackJack: %r, Splithand: %r, Soft: %r, Surrender: %r, Doubled: %r)" % (hand, status, hand.value, hand.busted(), hand.blackjack(), hand.splithand, hand.soft(), hand.surrender, hand.doubled)

        # print "Dealer Hand: %s (%d)" % (self.dealer.hand, self.dealer.hand.value)
        print self.player.strategy.qlearner.print_q()

    def get_money(self):
        return self.money

    def get_bet(self):
        return self.bet
