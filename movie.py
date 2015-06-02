class Movie:
    def __init__(self, title, director, genre, cost):
        self.title = title
        self.director = director
        self.genre = genre
        self.cost = cost

    def get_average(self):
        average = 0
        average = self.goals / self.games
        return average

    def show_details(self):
        print(self.title, "was directed by", self.director,". The genre was", self.genre, "and the movie production costed $", self.cost, ".")

#main routine
import doctest
doctest.testmod()
player1 = Movie ("The Maze Runner", "Wes Ball", "science fiction", 1000000)
player2 = Movie ("The Dark Knight", "Christopher Nolan", "superhero", 2000000)
player3 = Movie ("Little Miss Sunshine", "Jonathan Dayton and Valarie Ferris", "comedy-drama", 900000)
player1.show_details()
player2.show_details()
player3.show_details()
