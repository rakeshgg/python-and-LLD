import random

"""
Abstract classes is just a class never have a instances to it
class not instanciated class that is meant to act as base class
super class, parent class or to other classes in programing its
objective is soley increse the Abstarction of Programe into
conatins common inmplementaion details to other classes
similar to inheritance

Anstarct class have methods -
Abstract Methods not yet implemenetd by class but required
that to implement any class that inherit to it

Theoretically python doenot have notion of abstract class
we can't make abstract
not really a private attributes its just by convention
not to make instaces of it

"""


class AbstarctGame:
    # do not make instaces of it
    # abstarct is as general as it is
    # Game represention
    # common to all games
    # @staticmethod
    # concrete implemnetaion
    def start(self):
        while True:
            start = input("would you like to play")
            if start.lower() == "yes":
                break
        self.play()

    def end(self):
        print("The game has ended")
        self.reset()

    def play(self):
        # inforce child class to implemnts this methods
        # Anything inherit AbstarctGame need to override this
        # methods and provide impementaion
        raise NotImplementedError("provide impl to play()")

    # assume abstract methods
    def reset(self):
        raise NotImplementedError("provide impl to reset()")


# we have start and end and who is inheriting this should
# play, provide a Framework for every game play and reset
# Implented by game, start and end same as the way game start and end


# concrete class
# non abstract class, no abstarcts methods inside it
# actual thing we can use create instances
class RandomGusser(AbstarctGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    # override above
    def reset(self):
        self.round = 0

    # override above
    def play(self):
        while self.round < self.rounds:
            self.round += 1
            print(f" welcome to round {self.round}. lets begin!")
            random_num = random.randint(0, 10)
            while True:
                guess = input(" Entere a number 1-10 ")
                if int(guess) == random_num:
                    print(" ye got it")
                    break
        self.end()


game = RandomGusser(2)
game.start()


# implemnets other game
class AnotherGame(AbstarctGame):
    pass


# we have two games to play so may be we define a loops
# to play the buch of game
games = [RandomGusser(2), AnotherGame()]
# these all inherit from AbstarctGame
for game in games:
    game.start()
