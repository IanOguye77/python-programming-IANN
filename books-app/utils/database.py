# Concerned with storing and retrieving books from a list

books = []

# A function to  add a book into the list(database)
def add_books(name, author):
    books.append({
        'name': name, 
        'author': author,
        'read': False
    })

# function to get all the books
def get_all_books():
    return books


# function to mark book as read
def mark_book_as_read(name):
    for book in books:
        if book['name'].lower() == name.lower():
            book['read'] = True

            
# function to delete a book
def delete_book(name):
    for book in books:
        if book['name'].lower() == name.lower():
            books.remove(book)

    print(f"{book['name']} deleted successfully")