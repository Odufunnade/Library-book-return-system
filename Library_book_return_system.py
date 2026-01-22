returned_books = []

def return_book():
    student = input("Enter student name: ")
    book = input("Enter book title: ")
    returned_books.append({
        "student": student,
        "book": book
    })
    print("Book return recorded")

def view_returns():
    if not returned_books:
        print("No returned books recorded")
    else:
        for r in returned_books:
            print("Student:", r["student"], "| Book:", r["book"])

def main():
    while True:
        print("1. Return Book")
        print("2. View Returned Books")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            return_book()
        elif choice == "2":
            view_returns()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
