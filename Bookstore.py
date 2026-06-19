#this dictionary stores name and price of books
books={
    "Math":10,
    "Science":17,
    "English":20,
    "Python":0.1,
    "History":15
}

print("Welcome to Lohiths's Bookstore!")

bookname=input("Enter the name of the book you would like to purchase: ")

bookname_cap=bookname.capitalize().strip()
if bookname_cap in books:
    print(f"{bookname_cap} price is {books[bookname_cap]}")
else:
    print(f"{bookname_cap} was not found in the store please visit us in a few days!")