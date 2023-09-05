# Projects Brief
"""
    :Users' Story - I would/should like to do something so that i can achieve something
    NB: These user stories don't define the implementation of the application.
    
    As a user I would like to be able to:
    
    -> Add new movies to my collection
       : So I can keep track of all movies
    -> List all the movies in my collection
       : So I can see what movies I already have
    -> Find a movie by using the movie title
       : so I can locate a specific movie easily when the collection grows - (Searching)
    
    Implementation tasks - (How will we implement this Application) - (Decisions to make when you are creating the application)
    
    -> Decide where to store movies in code (Whether Databases, Dictionaries, Lists, variables, etc)
    -> Decide what data we want to store for each movie (Dictionaries representing movie properties, tuple with just the properties themselves and so on)
    -> Show the user a menu and let them pick an option(Decide what the user sees when they interact with our application)
    -> Implement each requirement in turn, each as a separate function
    -> Stop running the program when they type 'q' in the menu (Make sure that users can terminate the program)
    
    Finally lets start - 
    -> Where to store movies
       : Normally we would use a database, but we don't know how to yet!
    -> For now, store them in a Python list
       : This is easy (append, loop)
       : But movies get deleted from the collection when the app ends - (temporary compromise that we are going to make) --> movies = []
    -> What we store for each movie (How you want to represent the movie in your code e.g a dictionary that has keys e.g movie title, director; tuple where first value is title and director is the second value)
       : We'll create a dictionary for each movie
       : In the dictionary we'll store movie title, director, and release year
       : title = input("Enter the movie title: ")
         director = input("Enter the movie director: ")
         year = input("Enter the movie release_year: ")
         
         movies.append({
             'title': title,
             'director': director,
             'release_year': year
         })
         
    -> Show the user a menu
        : Get the user's input
        : Then run a while loop and get their input again at the end
        
        MENU_PROMPT = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit: ")
        selection = input(MENU_PROMPT)
        while selection != 'q':
            if selection == 'a':
                pass
            elif selection == 'l':
                pass
            elif selection == 'f':
                pass
            else:
                print("Unknown command. Please try again.")
                
            selection = input(MENU_PROMPT)
            
    -> Implement each requirement in turn (add movie, list movies and find movie)
        : Lets start coding and allow the users to add movies, list them, and find one by title
        : before that you can try this by yourself 
           

"""