from importer.StrategyImporter import StrategyImporter

IMPORTER = StrategyImporter('./csv/BasicStrategy.csv')
H, S, P = IMPORTER.import_player_strategy()
print("Importer Imported")

class BasicStrategy(object):
    """
    This is the known optimal policy for Blackjack without card counting
    """

    def __init__(self):
        self.hard_strat = H
        self.soft_strat = S
        self.pair_strat = P

    def record_result(self, **kwargs):
        pass

    def select_action(self, player, hand):
        if hand.soft():
            flag = self.soft_strat[hand.value][player.dealer_hand.cards[0].name]
        elif hand.splitable():
            flag = self.pair_strat[hand.value][player.dealer_hand.cards[0].name]
        else:
            flag = self.hard_strat[hand.value][player.dealer_hand.cards[0].name]
        return flag
