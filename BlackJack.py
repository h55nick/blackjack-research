import sys

import numpy as np
import scipy.stats as stats
import pylab as pl
import matplotlib.pyplot as plt

from Player import Player
from Dealer import Dealer
from Game import Game

from RLStrategy import RLStrategy
from BasicStrategy import BasicStrategy
from RandomStrategy import RandomStrategy

GAMES = 100

if __name__ == "__main__":
    print sys.argv[1]
    if sys.argv[1] == 'random':
        print "Random Strategy"
        strategy = RandomStrategy()
    elif sys.argv[1] == 'basic':
        print "Basic Strategy"
        strategy = BasicStrategy()
    elif sys.argv[1] == 'rl':
        print "Reinforcement Strategy"
        strategy = RLStrategy()
    else:
        print "Random Strategy"
        strategy = RandomStrategy()

    moneys = []
    bets = []
    countings = []
    nb_hands = 0
    for g in range(GAMES):
        game = Game(strategy)
        while not game.shoe.reshuffle:
            # print '%s GAME no. %d %s' % (20 * '#', i + 1, 20 * '#')
            game.play_round()
            nb_hands += 1

        moneys.append(game.get_money())
        bets.append(game.get_bet())
        countings += game.shoe.count_history

        print("WIN for Game no. %d: %s (%s bet)" % (g + 1, "{0:.2f}".format(game.get_money()), "{0:.2f}".format(game.get_bet())))

    sume = 0.0
    total_bet = 0.0
    for value in moneys:
        sume += value
    for value in bets:
        total_bet += value

    print strategy.qlearner.print_q()
    print "\n%d hands overall, %0.2f hands per game on average" % (nb_hands, float(nb_hands) / GAMES)
    print "%0.2f total bet" % total_bet
    print("Overall winnings: {} (edge = {} %)".format("{0:.2f}".format(sume), "{0:.3f}".format(100.0*sume/total_bet)))

    # moneys = sorted(moneys)
    # fit = stats.norm.pdf(moneys, np.mean(moneys), np.std(moneys))  # this is a fitting indeed
    # pl.plot(moneys, fit, '-o')
    # pl.hist(moneys, normed=True)
    # pl.show()
    #
    # plt.ylabel('count')
    # plt.plot(countings, label='x')
    # plt.legend()
    # plt.show()
