import pickle
infile = open("Game.dat", 'rb')
savedgame = pickle.load(infile)
infile.close()
