from utils import database

USER_CHOICE = """
Enter:

-'a' to add a new book
- 'l' to list all the books
- 'r' to mark as read
- 'd' to delete a book
- 'q' to quit

Enter Your Choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            show_book()
        elif user_input == 'r':
           prompt_mark_book_as_read()
        elif user_input == 'd':
            prompt_delete_books()
        else:
            print("Unknown Choice. Please Try Again!!!")
        user_input = input(USER_CHOICE)

# call a function to prompt the user to add a new book
def prompt_add_book():
    name = input("Enter the name of the new book: ")
    author = input("Enter the author of the new book: ")
    database.add_books(name, author)
# call a function to allow the user list all books
def show_book():
    books = database.get_all_books()
    if len(books) > 0:
        # s = "s" if len()
        for book in books:
            read = "YES" if book['read'] == '1' else "NO" # ternary operator/ shorthand if statement
            # read == None
            # if book['read'] == True:
            #     read == "YES"
            # else:
            #     read = "NO"
            print(f"{book['name']} written by {book['author']}, read: {read}")   
    else:
        print("You have no books at the moment.")
# call a function to prompt the user to mark a book as read
def prompt_mark_book_as_read():
    name = input("Enter the name of the book you've finished reading: ")
    database.mark_book_as_read(name)
# call a function to prompt the user to delete a book
def prompt_delete_books():
    name = input("Enter the name of the book you wish to delete: ")
    database.delete_book(name)

# call the menu function
menu()