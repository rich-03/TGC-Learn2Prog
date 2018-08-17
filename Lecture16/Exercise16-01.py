import random
from matplotlib.pyplot import show, hist

rolls = []
for i in range(10000):
    roll = (random.randrange(6) + 1) + (random.randrange(6) + 1) + (random.randrange(6) + 1)
    rolls.append(roll)
hist(rolls, bins=16)
show()
