class Library:
    def __init__(self):
       self.file_path="books.txt"
       self.file=open(self.file_path,"a+")
    def __del__(self):
        if self.file:
            self.file.close()
    def addBook(self):
        self.file.seek(0)
        books_info=self.file.read().splitlines()

        if books_info:
            print("Books in the library")
            for book in books_info:
                    title,author,relase_year,num_pages=book_info.split(',')
                    print(f"Title:{title},Author:{author},Release Year:{release_year},Pages:{num_pages}")
        else:
            print("No books found")

    def add_book(self):
                title=input("enter title of book")
                author=input("enter book author")
                release_year=input("enter first book release year")
                num_pages=input("enter number of pages")

                book_info=f"{title},{author},{release_year},{num_pages}\n"
                self.file.seek(0)
                books_info=self.file.read().splitlines()

                updated_books=[book + '\n' for book in books_info if title_to_remove not in book]

                self.file.seek(0)
                self.file.truncate()
                for updated_book in updated_books:
                    self.file.write(update_book)

                print(f"book'{title_to_remove}' removed succesfully")

lib=Library()

while True:
    print("\n***MENU***")
    print("1) list books")
    print("2) add books")
    print("3) remove book")
    print("4) exit")

    choice=input("enter your choice(1-4)")
    if choice=="1":
       lib.list_books()
    elif choices=="2":
        lib.add_book()
    elif choices=="3":
        lib.remove_book()
    elif choices=="4":
        print("exiting the program. goodbye")
        break
    else:
        print("invalid choice. please try again")

