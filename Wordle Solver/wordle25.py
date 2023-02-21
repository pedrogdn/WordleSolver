
from array import *
from itertools import groupby
import random


bank1 = list()
with open('fiveLetterWords.txt') as f:
    for line in f:
            bank1.append(line.rstrip('\n'))

for i in range(len(bank1)):
        bank1[i] = bank1[i].upper()


print (len(bank1), "words loaded.\n")

print ("CRANE recommended for 1st word.")
print ("TOILS recommended for 2nd word.")

word1 = "CRANE"

res = bank1

wordle = input("\nPress (t) to type a word, or (s) for a suggestion: ")

if wordle == 't':
        word1 = input()
        word1 = word1.upper()
        print(word1)
        
if wordle == 's':
        print("Try: ", word1)

for h in range(6):


        yFilter = []
        elim = []
        fbi = ['i'] * 5

        fbi[0] = input('Feedback for letter 1 (g, y or b): ')
        fbi[1] = input('Feedback for letter 2 (g, y or b): ')
        fbi[2] = input('Feedback for letter 3 (g, y or b): ')
        fbi[3] = input('Feedback for letter 4 (g, y or b): ')
        fbi[4] = input('Feedback for letter 5 (g, y or b): ')

        if fbi[0] == 'b':
                for g in range(5):
                        if (fbi[g] == 'g' or fbi[g] == 'y') and (word1[g] == word1[0]):
                                fbi[0] = 'p'
                                
        if fbi[1] == 'b':
                for g in range(5):
                        if (fbi[g] == 'g' or fbi[g] == 'y') and (word1[g] == word1[1]):
                                fbi[1] = 'p'
                                
        if fbi[2] == 'b':
                for g in range(5):
                        if (fbi[g] == 'g' or fbi[g] == 'y') and (word1[g] == word1[2]):
                                fbi[2] = 'p'
                                
        if fbi[3] == 'b':
                for g in range(5):
                        if (fbi[g] == 'g' or fbi[g] == 'y') and (word1[g] == word1[3]):
                                fbi[3] = 'p'
                                
        if fbi[4] == 'b':
                for g in range(5):
                        if (fbi[g] == 'g' or fbi[g] == 'y') and (word1[g] == word1[4]):
                                fbi[4] = 'p'



        if fbi[0] == 'b':
            elim.append(word1[0])

        if fbi[1] == 'b':
            elim.append(word1[1])

        if fbi[2] == 'b':
            elim.append(word1[2])

        if fbi[3] == 'b':
            elim.append(word1[3])

        if fbi[4] == 'b':
            elim.append(word1[4])


        res = [ele for ele in res if all(ch not in ele for ch in elim)]


        if fbi[0] == 'y':
            yFilter.append(word1[0])

        if fbi[1] == 'y':
            yFilter.append(word1[1])

        if fbi[2] == 'y':
            yFilter.append(word1[2])

        if fbi[3] == 'y':
            yFilter.append(word1[3])

        if fbi[4] == 'y':
            yFilter.append(word1[4])

        res = [ele for ele in res if all(ch in ele for ch in yFilter)]

        if fbi[0] == 'y':
            res = [x for x in res if x[0] != word1[0]]

        if fbi[1] == 'y':
            res = [x for x in res if x[1] != word1[1]]

        if fbi[2] == 'y':
            res = [x for x in res if x[2] != word1[2]]

        if fbi[3] == 'y':
            res = [x for x in res if x[3] != word1[3]]

        if fbi[4] == 'y':
            res = [x for x in res if x[4] != word1[4]]


        if fbi[0] == 'p':
            res = [x for x in res if x[0] != word1[0]]

        if fbi[1] == 'p':
            res = [x for x in res if x[1] != word1[1]]

        if fbi[2] == 'p':
            res = [x for x in res if x[2] != word1[2]]

        if fbi[3] == 'p':
            res = [x for x in res if x[3] != word1[3]]

        if fbi[4] == 'p':
            res = [x for x in res if x[4] != word1[4]]


        if fbi[0] == 'g':
            res = [x for x in res if x[0] == word1[0]]

        if fbi[1] == 'g':
            res = [x for x in res if x[1] == word1[1]]

        if fbi[2] == 'g':
            res = [x for x in res if x[2] == word1[2]]

        if fbi[3] == 'g':
            res = [x for x in res if x[3] == word1[3]]

        if fbi[4] == 'g':
            res = [x for x in res if x[4] == word1[4]]

        print ("The filtered strings are : " + str(res),"\n")
        print (len(res),  "words filtered.\n")

        word1 = random.choice(res)

        wordle = input("Press (t) to type a word, or (s) for a suggestion: ")

        if wordle == 't':
                word1 = input()
                word1 = word1.upper()
                print(word1)
                
        if wordle == 's':
                print("Try: ", word1)
                rand = input("Type (n) to generate a new word or ENTER to continue...")
                while rand == 'n':
                        word1 = random.choice(res)
                        print ("Try: ", word1)
                        rand = input("Type (n) to generate a new word or ENTER to continue...")



                
