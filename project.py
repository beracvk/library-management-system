class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        if self.file:
            self.file.close()

    def list_books(self):
        self.file.seek(0)
        books_info = self.file.read().splitlines()

        if books_info:
            print("Books in the library:")
            for book_info in books_info:
                title, author, release_year, num_pages = book_info.split(',')
                print(f"Title: {title}, Author: {author}, Release Year: {release_year}, Pages: {num_pages}")
        else:
            print("No books in the library")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books_info = self.file.read().splitlines()

        updated_books = [book + '\n' for book in books_info if title_to_remove not in book]

        self.file.seek(0)
        self.file.truncate()
        for updated_book in updated_books:
            self.file.write(updated_book)

        print(f"Book '{title_to_remove}' removed successfully.")


# Create Library object
lib = Library()


# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
