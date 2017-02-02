## BlackJack-Research
==============================================

Basic BlackJack implementation with ability to add various strategies.

BlackJack implementation cloned from: git@github.com:seblau/BlackJack-Simulator.git with modifications (ie. no Omega, etc)

### Running

    `python BlackJack.py`

### Gaming Rules

The simulator plays with the following casino rules:

* Dealer stands on soft 17
* Double down after splitting hands is allowed
* No BlackJack after splitting hands
* 3 times 7 is counted as a BlackJack

### Configuration Variables

At top of BlackJack.py

| Variable        | Description         |
| ------------- |-------------|
| *GAMES*  | The number of games that should be played |
| *ROUNDS_PER_GAME*  | The number of rounds that should be played per game (may cover multiple shoes) |
| *SHOE_SIZE*   | The number of decks that are used |
| *SHOE_PENETRATION*  | Indicates the percentage of cards that still remain in the shoe, when the shoe gets reshuffled |
| *BET_SPREAD*  | The multiplier for the bet size in a player favorable counting situation |

### Strategy

Any strategy can be fed into the simulator as a .csv file. The default strategy that comes with this simulator looks like the following:

![Default Strategy](/documentation/strategy.png?raw=true)

* The first column shows both player's cards added up
* The first row shows the dealers up-card
* S ... Stand
* H ... Hit
* Sr ... Surrender
* D ... Double Down
* P ... Split
