import random

bank1 = []
with open('fiveLetterWords.txt') as f:
    bank1 = [line.strip().upper() for line in f]

print(len(bank1), "words loaded.\n")

print("CRANE recommended for 1st word.")
print("TOILS recommended for 2nd word.")

word1 = "CRANE"

wordle = input("\nPress (t) to type a word, or (s) for a suggestion: ")

if wordle == 't':
    word1 = input().upper()
    print(word1)

elif wordle == 's':
    print("Try:", word1)

for h in range(6):
    yFilter = []
    elim = []
    fbi = ['i'] * 5

    for i in range(5):
        fbi[i] = input('Feedback for letter {} (g, y or b): '.format(i + 1))

    for g in range(5):
        if fbi[g] == 'b' or fbi[g] == 'y':
            if word1[g] == word1[g]:
                fbi[g] = 'p'

    elim = [ch for ch, fb in zip(word1, fbi) if fb == 'b']
    res = [ele for ele in bank1 if not any(ch in ele for ch in elim)]

    yFilter = [ch for ch, fb in zip(word1, fbi) if fb == 'y']
    res = [ele for ele in res if all(ch in ele for ch in yFilter)]
    res = [x for x in res if all(x[i] != word1[i] for i, fb in enumerate(fbi) if fb == 'y')]
    res = [x for x in res if all(x[i] != word1[i] for i, fb in enumerate(fbi) if fb == 'p')]
    res = [x for x in res if all(x[i] == word1[i] for i, fb in enumerate(fbi) if fb == 'g')]

    print("The filtered strings are:", res, "\n")
    print(len(res), "words filtered.\n")

    word1 = random.choice(res)

    wordle = input("Press (t) to type a word, or (s) for a suggestion: ")

    if wordle == 't':
        word1 = input().upper()
        print(word1)

    elif wordle == 's':
        print("Try:", word1)
        rand = input("Type (n) to generate a new word or ENTER to continue...")
        while rand == 'n':
            word1 = random.choice(res)
            print("Try:", word1)
            rand = input("Type (n) to generate a new word or ENTER to continue...")
