from platform import node

import neck as neck
import pip._vendor.requests

nodelist = []
n = node(pip._vendor.requests.head)
nodelist.append(n)
n = node(neck)
nodelist.append(n)


def torso():
    pass


n = node(torso)
nodelist.append(n)


def arm():
    pass


n = node(arm)
nodelist.append(n)


def hand():
    pass


n = node(hand)
nodelist.append(n)


def leg():
    pass


n = node(leg)
nodelist.append(n)


def foot():
    pass


n = node(foot)
nodelist.append(n)

root = 0
for i in range(1, 7):
    nodelist[root].insert(i)
nodelist[root].printinorder()
