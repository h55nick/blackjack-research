import random

class RLStrategy(object):
    """
    Reinforcement Learner
    """

    def __init__(self):
        actions = ['D', 'Sr', 'H', 'S'] # , 'P'
        self.qlearner = QLearn(actions)
        self.last_action = None

    def q(self):
        self.qlearner.q

    def create_state(self, hand, player):
        return "{}|{}".format(hand.card_values(), player.dealer_hand.first_card())

    def record_result(self, hand, player, win=None):
        state = self.create_state(hand, player)
        state1 = self.last_state
        action = self.last_action
        if win == None:
            reward = self.qlearner.getQ(state, action)
        else:
            reward = win
        print "state: {}, action {}, reward: {}, state1: {}".format(state, action, reward, state1)
        self.qlearner.learn(state, action, reward, state1)
        self.last_state = ""
        return ''

    def select_action(self, player, hand):
        # print self.qlearner.q
        state =  self.create_state(hand, player)
        self.last_action = self.qlearner.chooseAction(state)
        self.last_state = state
        return self.last_action

class QLearn:
    """
    Abstract Q Leaner
    """

    def __init__(self, actions, epsilon=0.6, alpha=0.2, gamma=0.99):
        self.q = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = actions

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learnQ(self, state, action, reward, value):
        oldv = self.q.get((state, action), None)
        if oldv is None:
            self.q[state, action] = reward
        else:
            self.q[state, action] = oldv + self.alpha * (value - oldv)
        return

    def chooseAction(self, state):
        print state
        if False and random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [ self.getQ(state, a) for a in self.actions ]
            maxQ = max(q)
            print maxQ
            count = q.count(maxQ)
            if count > 1:
                best = [ i for i in range(len(self.actions)) if q[i] == maxQ ]
                i = random.choice(best)
            else:
                i = q.index(maxQ)
            action = self.actions[i]
        return action

    def learn(self, state1, action1, reward, state2):
        maxqnew = max([ self.getQ(state2, a) for a in self.actions ])
        self.learnQ(state1, action1, reward, reward + self.gamma * maxqnew)

    def print_q(self):
        for k in sorted(self.q, key=lambda k: k):
            print "k: {}  | {}".format(k, self.q[k])

