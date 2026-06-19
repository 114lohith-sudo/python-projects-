sentence = input("Enter a sentence: ").lower()

letters = {}

for letter in "abcdefghijklmnopqrstuvwxyz":
    letters[letter] = False

for char in sentence:
    if char in letters:
        letters[char] = True

pangram = True

for letter in letters:
    if letters[letter] == False:
        pangram = False
        break

if pangram == True:
    print("This is a pangram!")
else:
    print("This is not a pangram.")