from __future__ import division

usr = raw_input('Enter a word: ')
usr = usr.upper()

letter = 0
vowels = 0

vowelList = ['A', 'E', 'I', 'O', 'U']

for i in usr:
    isVowel = False
    letter = letter + 1
    for x in vowelList:
        if x == i:
            isVowel = True
    if isVowel:
        vowels = vowels + 1
perc = vowels / letter

print("Letters: " + str(letter))
print("Vowels: " + str(vowels))
print("Percentage of vowels: " + str("{0:.2f}".format(vowels / letter * 100)))

