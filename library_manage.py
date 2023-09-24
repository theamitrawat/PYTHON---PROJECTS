class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        no_of_books = int(input("\nEnter the number of books: "))
        for i in range(no_of_books):
            book_name = input(f"\t{i + 1} Book name: ")
            self.books.append(book_name)

    def view_no_of_books(self):
        print(f"\n\tNumber of Books in Library: {len(self.books)}")

    def view_book(self):
        print("\nBooks in the library are:")
        for i, b in enumerate(self.books):
            print(f"\t{i + 1}. {b}")

    def remove_book(self):
        book_id = int(input("\nEnter the book ID to remove: "))
        if book_id >= 1 and book_id <= len(self.books):
            removed_book = self.books.pop(book_id - 1)
            print(f"\n\tRemoved book with ID {book_id}: {removed_book}")
        else:
            print("Invalid book ID. No book removed.")

    def update_book(self):
        book_id = int(input("\nEnter the book ID to update: "))
        if book_id >= 1 and book_id <= len(self.books):
            new_book_name = input("Enter the new book name: ")
            old_book_name = self.books[book_id - 1]
            self.books[book_id - 1] = new_book_name
            print(f"\n\tUpdated book with ID {book_id}: '{old_book_name}' to '{new_book_name}'")
        else:
            print("Invalid book ID. No book updated.")

def main():
    lib = Library()
    while True:
        print("\n1. Add Book.")
        print("2. View no. of Books")
        print("3. View Book")
        print("4. Remove Book")
        print("5. Update Book")
        print("6. Quit")

        user_choice = input("\n---> Enter your choice: ")

        choice_list = ['1', '2', '3', '4', '5', '6']
        if user_choice in choice_list:
            match user_choice:
                case '1':
                    lib.add_book()
                case '2':
                    lib.view_no_of_books()
                case '3':
                    lib.view_book()
                case '4':
                    lib.remove_book()
                case '5':
                    lib.update_book()
                case '6':
                    print("\n~ Thanks for using the library. Please use it again soon! ~")
                    print("\n--------------------------------------------------------")
                    break
        else:
            print("\n\tInvalid option. Please choose a correct option.")
            print("\n--------------------------------------------------------")


if __name__ == "__main__":
    main()
