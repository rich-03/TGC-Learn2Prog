import pickle

import tetris as tetris

outfile = open("Game.dat", 'wb')
pickle.dump(tetris, outfile)
outfile.close()
