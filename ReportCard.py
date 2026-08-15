students = (
    ("Vihaan", 85, 90, 88, 92),
    ("Arnay", 78, 82, 80, 75),
    ("Lohith", 95, 93, 97, 96),
    ("Atarv", 88, 84, 91, 87)
)

search_name = input("Enter the student's name: ")

found = False

for student in students:
    if student[0].lower() == search_name.lower():
        print("\nStudent Report Card:")
        print(student)
        found = True
        break

if not found:
    print("Sorry, that student is not in the report card.")