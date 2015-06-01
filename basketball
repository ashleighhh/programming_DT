class BasketballPlayer:
    def __init__(self, name, games, goals):
        self.name = name
        self.games = games
        self.goals = goals

    def get_average(self):
        average = 0
        average = self.goals / self.games
        return average

    def show_average(self):
        print("The average amount of goals scored per game by ", self.name, "is", self.goals / self.games)

#main routine
import doctest
doctest.testmod()
player1 = BasketballPlayer ("Karen", 20, 80)
player2 = BasketballPlayer ("Anna", 40, 60)
player3 = BasketballPlayer ("Tim", 15, 30)
player1.show_average()
player2.show_average()
player3.show_average()
