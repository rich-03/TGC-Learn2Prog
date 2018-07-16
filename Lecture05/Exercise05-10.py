correct_number = 5

guess = int(input("Your guess?"))

while guess != correct_number:
    guess = int(input("Wrong :( your guess?"))

print("You guessed it right!")
