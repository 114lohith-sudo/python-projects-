
text=input("Enter a string: ")

vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for read in text:
    if read in vowels:
        vowels[read]+=1
print(vowels)