import random

#Generate a random number between 0-1
print(random.random())

# Returns an integer. bewteen 1-100
print(random.randint(1,100))

#Generate 2 random integers bw 1 and 20
for i in [ 1, 2]:
    print(random.randint(1,20))


class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        res = (dice1 , dice2)
        # return dice1, dice2           # This will also work.
        return res

a = Dice()
print(a.roll())



