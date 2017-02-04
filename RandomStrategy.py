import random

class RandomStrategy(object):
    """
    Randomly do actions
    """

    def __init__(self):
        pass

    def record_result(self, **kwargs):
        pass

    def select_action(self, player, hand):
        options = ['D', 'Sr', 'H', 'P', 'S']
        return random.choice(options)
