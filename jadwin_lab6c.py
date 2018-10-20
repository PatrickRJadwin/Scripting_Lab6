import random as r

print('1st roll...')

inp1 = raw_input('Welcome to Craps! Enter Y for the first roll!\n')
print('\n')

if inp1.upper() != 'Y':
    print('Goodbye')
    exit(0)


def roll():
    dice = [r.randint(1, 6), r.randint(1, 6)]
    print('roll 1: ' + str(dice[0]))
    print('roll 2: ' + str(dice[1]))
    total = dice[0] + dice[1]
    print('\ntotal: ' + str(total) + "\n")
    return total


print('1st roll for user...')

roll1 = roll()

if roll1 == 7 or roll1 == 11:
    print('You win on the first roll!')
    exit(0)

if roll1 == 2 or roll1 == 3 or roll1 == 12:
    print('You lose on the first roll!')
    exit(0)

print('1st roll for computer...')

roll2 = roll()

if roll2 == 7 or roll2 == 11:
    print('Computer wins on the first roll! You lose!')
    exit(0)

if roll2 == 2 or roll2 == 3 or roll2 == 12:
    print('Computer loses on the first roll! You win!')
    exit(0)

keepplaying = raw_input('Keep playing? (Y for yes, N for no)\n')
print('\n')

if keepplaying != 'y':
    print('Goodbye')
    exit(0)

rollcount = 1
isMatch = False
comp = False
usr = False
usertracker = 0
while isMatch == False:
    if usertracker % 2 == 0:
        print('User Turn...')
    else:
        print('Comp Turn...')
    roll3 = roll()
    rollcount = rollcount + 1
    if usertracker % 2 == 0:
        if roll3 == roll1:
            isMatch = True
            usr = True
            break
        if roll3 == 7:
            usr = True
            break
    else:
        if roll3 == roll2:
            isMatch = True
            comp = True
            break
        if roll3 == 7:
            comp = True
            break
    kpplay = raw_input('Keep playing? (Y for yes, N for no)\n')
    print('\n')
    if kpplay == 'y':
        usertracker = usertracker + 1
        continue
    else:
        print('goodbye!')
        exit(0)

if isMatch and usr:
    print('You win!')
    print('It took ' + str(rollcount) + ' rolls to win!')

if isMatch is False and usr:
    print('You rolled a 7 and lost')


if isMatch and comp:
    print('Computer win!')
    print('It took ' + str(rollcount) + ' rolls to win!')

if isMatch is False and comp:
    print('Computer rolled a 7 and lost')

