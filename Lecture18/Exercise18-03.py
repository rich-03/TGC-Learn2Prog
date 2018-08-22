class Game:
    name = ""
    numplayers = 0


class Videogame(Game):
    platform = ""

    def print(self):
        pass


tetris = Videogame()
tetris.name = "Tetris"
tetris.numplayers = 1
tetris.platform = "Windows"
tetris.print()
