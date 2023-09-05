# Create a menu for the user to choose from
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie by title, or 'q' to quite:"

# Create an empty list to store the movies
movies = []

# a function to add a movie
def add_movie():
    # Prompt the user for movie properties
    title = input("Enter The Movie Title:")
    director = input("Enter The Movie Director:")
    year = input("Enter The Movie Release Year:")

    movies.append({
        'title' : title,
        'director' : director,
        'year' : year,
    })

# a function to list all movie
def list_movies():
# hint use a for loop
    for movie in movies:
        print_movie(movie)

# a function to find a movie by its title
def find_movie():
    movie_title= input("Enter the movie title you wish to find: ")
    for movie in movies:
        if movie['title'].lower() == movie_title.lower():
            print(f"{movie['title']} directed by {movie['director']}, was released in {movie['year']}")

   


# create a helper function to display the movie
def print_movie(movie):
    # print(f"Movie Title: {movie['title']}")
    # print(f"Movie Director: {movie['director']}")
    # print(f"Release Year: {movie['year']}")
    print(f"{movie['title']} directed by {movie['director']}, was released in {movie['year']}")
# create a function to display the menu
def menu():
# get the user choice
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Unknown Command, Please Try Again.")
        selection = input(MENU_PROMPT)    

# remeber to run the menu function at the end
menu()        