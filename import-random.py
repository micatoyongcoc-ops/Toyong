class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrower = None

    def borrow(self, member):
        if self.is_available:
            self.is_available = False
            self.borrower = member
            return True
        return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            self.borrower = None
            return True
        return False

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrower.name}"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - Borrowed: {[b.title for b in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def list_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(member)

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Members")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")
        
        elif choice == "2":
            name = input("Enter member name: ").strip()
            member_id = input("Enter member ID: ").strip()
            member = Member(name, member_id)
            library.add_member(member)
            print("Member added successfully.")
        
        elif choice == "3":
            member_id = input("Enter member ID: ").strip()
            member = library.find_member(member_id)
            if not member:
                print("Member not found.")
                continue
            isbn = input("Enter book ISBN: ").strip()
            book = library.find_book(isbn)
            if not book:
                print("Book not found.")
                continue
            if member.borrow_book(book):
                print(f"{member.name} borrowed '{book.title}'.")
            else:
                print("Book is not available.")
        
        elif choice == "4":
            member_id = input("Enter member ID: ").strip()
            member = library.find_member(member_id)
            if not member:
                print("Member not found.")
                continue
            isbn = input("Enter book ISBN: ").strip()
            book = library.find_book(isbn)
            if not book:
                print("Book not found.")
                continue
            if member.return_book(book):
                print(f"{member.name} returned '{book.title}'.")
            else:
                print("Return failed (book not borrowed by this member).")
        
        elif choice == "5":
            print("\nBooks in library:")
            library.list_books()
        
        elif choice == "6":
            print("\nMembers:")
            library.list_members()
        
        elif choice == "7":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()