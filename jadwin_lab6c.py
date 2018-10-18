import random as r

print('1st roll...')


def roll():
    dice = [r.randint(1, 6), r.randint(1, 6)]
    print('roll 1: ' + str(dice[0]))
    print('roll 2: ' + str(dice[1]))
    total = dice[0] + dice[1]
    print('\ntotal: ' + str(total) + "\n")
    return total


roll1 = roll()

if roll1 == 7 or roll1 == 11:
    print('You win on the first roll!')
    exit(0)

if roll1 == 2 or roll1 == 3 or roll1 == 12:
    print('You lose on the first roll!')
    exit(0)

print('2nd roll...')
rollcount = 1
isMatch = False
while isMatch == False:
    roll2 = roll()
    rollcount = rollcount + 1
    if roll2 == roll1:
        isMatch = True
    if roll2 == 7:
        break

if isMatch:
    print('You win!')
    print('It took ' + str(rollcount) + ' rolls to win!')

if isMatch == False:
    print('You rolled a 7 and lost')
