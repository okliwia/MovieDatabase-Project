from movie import Movie
import csv
import re

def main():
    movies = []
    menu(movies)

def menu(movies):
    while True:
        print("""===========================
1. Display movie          =
2. Add new movie          =
3. Edit movie             =
4. Delete movie           =
5. List movies            =
6. Rate movie             =
7. Rank movies            =
8. Show stats             =
9. Import movies          =
10. Export movies         =
11. Exit                  =
===========================""")
        option = input()
        if option == "1":
            title = input("Type movie title: ")
            display_movie(movies, title)
        elif option == "2":
            add_movie(movies)
        elif option == "3":
            title = input("Type movie title: ")
            edit_movie(movies, title)
        elif option == "4":
            title = input("Type movie title: ")
            delete_movie(movies, title)
        elif option == "5":
            expression = input("Type regex expression:")
            list_movies(movies, expression)
        elif option == "6":
            title = input("Type movie title: ")
            rate_movie(movies, title)
        elif option == "7":
            rank_movies(movies)
        elif option == "8":
            stats(movies)
        elif option == "9":
            path = input("Type path to import from: ")
            movies = import_movies(movies, path)
        elif option == "10":
            path = input("Type path to export into: ")
            export_movies(movies, path)
        elif option == "11":
            return 0

def add_movie(movies):
    title = input("Title: ")
    director = input("Director: ")
    genre = input("Choose genre (horror, drama, tv series, slasher, documentary, thriller, action, animation):")
    actors = []
    while True:
        cast_member = input("Actor/Actress (if finished put empty string):")
        if cast_member == "":
            break
        actors.append(cast_member)
    poster_url = input("Poster URL: ")
    movie = Movie(title=title.strip(), director=director.strip(), genre=genre.strip(),actors=actors,poster_url=poster_url.strip())
    movies.append(movie)

def list_movies(movies, expression):
    results = []
    for movie in movies:
        matched = re.match(expression, movie.title)
        if bool(matched):
            results.append(movie)
    for movie in results:
        movie.print()

def edit_movie(movies, title):
    movie, index = display_movie(movies, title)
    decision = input("What you want to edit? (T - title, D - director, G - genre ,A - actors, P - poster URL)")
    if decision == "T":
        new_title = input("Type new title: ")
        movies[index].title = new_title
    elif decision == "D":
        new_director = input("Type new director: ")
        movies[index].director = new_director
    elif decision == "G":
        new_genre = input("Type new genre: ")
        movies[index].genre = new_genre
    elif decision == "A":
        new_actors = input("Type new actors: ")
        movies[index].actors = new_actors
    elif decision == "P":
        new_url = input("Type new url: ")
        movies[index].actors = new_url

def delete_movie(movies, title):
    movie, index = display_movie(movies, title)
    while True:
        decision = input("Do you want to delete the above movie? (YES/NO)")
        if decision == "YES":
            movies.pop(index)
            print("Movie was removed.")
            break
        elif decision == "NO":
            break

def display_movie(movies, title):
    movie, index = find_movie(movies, title)
    if movie is None:
        print("The movie is not in the database.")
    else:
        movie.print()
    return movie, index

def find_movie(movies, title):
    index = 0
    for movie in movies:
        if movie.title == title.strip():
            return movie, index
        index += 1
    return None, None

def rate_movie(movies, title):
    movie, index = display_movie(movies, title)
    rating = int(input("Rate above movie out of 10: "))
    if index is None:
        print("The movie is not in the database.")
        return
    if rating <= 10:
        movies[index].ratings.append(rating)
        print("Rating saved succesfully!")
    else:
        print("Incorrect rating!")

def rank_movies(movies):
    movies.sort(key=lambda movie: movie.calculate_rating(), reverse=True)
    place = 1
    for movie in movies:
        if movie.ratings:
            print(f"{place}.",end='')
            movie.print()
            place += 1

def stats(movies):
    categories = {'action': 0, 'horror': 0, 'thriller': 0, 'animation': 0, 'comedy': 0, 'drama': 0, 'documentary': 0, 'slasher': 0, 'tv series': 0}
    for movie in movies:
        categories[movie.genre] = categories[movie.genre] + 1
    print(categories)

def import_movies(movies, path):
    with open(path, "r") as f:
        reader = csv.DictReader(f,delimiter='\t')
        movies = [] 
        for row in reader:
            actors = []
            for actor in row['Actors'].strip('[]').split(','):
                actors.append(actor.strip(' \'')) 
            movie = Movie(row['Title'], row['Director'],row['Genre'],actors, row['URL'])
            if row['Ratings']:
                ratings_string = row['Ratings'].strip('[]').split(',')
                ratings = []
                for rating in ratings_string:
                    ratings.append(int(rating))
                movie.ratings = ratings
            else:
                movie.ratings = []
            movies.append(movie)
        return movies

def export_movies(movies, path):
    header = ['Title', 'Director', 'Genre', 'Actors' ,'URL','Ratings']
    with open(path, 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f,delimiter='\t')
        writer.writerow(header)
        for movie in movies:
            if movie.ratings: 
                writer.writerow([movie.title, movie.director, movie.genre, movie.actors, movie.poster_url, movie.ratings])
            else:
                 writer.writerow([movie.title, movie.director, movie.genre, movie.actors, movie.poster_url, None])

if __name__ == "__main__":
    main()
