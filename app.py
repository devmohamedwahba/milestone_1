"""
- Enter 'a' to add movie 'l' to see your movies 'f' to find movie and 'q' to quit :

- add movies
- see movies
- find movie
- stop running the program
Tasks :
[x]: Decide Where to store movies
[x]: what is the format of movie ?
[x]: Show Yhe user main interface and get their input
[x]: Allow users to add movies
[x]: Show all their movies
[]: find a movie
[x]: stop running the program when they type 'q'
"""
movies = []


def menu():
    user_input = input("Enter 'a' to add movie 'l' to see your movies 'f' to find movie and 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown Please try again')
        user_input = input("\nEnter 'a' to add movie 'l' to see your movies 'f' to find movie and 'q' to quit: ")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')
    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movie_list):
    for movie in movie_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")
    print('=============================')


def find_movie():
    find_by = input('What is property of movie are you looking for ? ')
    looking_for = input('what are you searching for? ')
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


if __name__ == '__main__':
    menu()
