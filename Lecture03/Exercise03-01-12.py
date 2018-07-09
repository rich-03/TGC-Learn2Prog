a = 1
b = 2
c = 2
d = "One"
e = "Two"
f = "Three"
g = "one"

a > b # False
a == b # False
a != b # True
b == c # True
d < e # True
e < f # True
d < g # False
g < e # True
not (a == b) # True
b < c or b > c # False
(a+1) == b and not b < c # True
((a <= b) and (b <= c)) or ((a >= b) and (b >= c)) # False