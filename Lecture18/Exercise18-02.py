class Game:
    name = ""
    numplayers = 0


class Videogame(Game):
    platform = ""


def print(self):
    print(self.name)
    print("Up to", self.numplayers, "players")
    print("Can be played on", self.platform)


class Boardgame(Game):
    numpieces = 0
    board = [0, 0]


def print(self):
    print(self.name)
    print("Up to", self.numplayers, "players")
    print("Has", self.numpieces, "pieces, and a board of size", self.board[0], "by", self.board[1])
