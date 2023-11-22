# Concerned with storing and retrieving books from a list

books = []
file = "books.txt"

# A function to  add a book into the list(database)
def add_books(name, author):
    with open(file, 'a') as f:
        f.write(f"{name},{author},0\n")

# function to get all the books
def get_all_books():
    with open(file, 'r') as f:
        lines = [line.strip('\n').split(',') for line in f.readlines()]
        books = [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]
        return books

# function to mark book as read
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)

# A function to save all books in the file
def _save_all_books(books):
    with open(file, 'w') as f:
        for book in books:
            f.write(f"{book['name']},{book['author']},{book['read']}\n")


# function to delete a book
def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name] 
    _save_all_books(books)