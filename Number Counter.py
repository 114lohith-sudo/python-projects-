#give a phone number to this project
#give count for each number from 0 to 9
phone_number=input("Enter you phone number: ")
numbers = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}
for num in phone_number:
    if num in numbers:
        numbers[num]+=1

print(numbers)