class Movie:
    genre = ""
    director = ""
    title = ""
    poster_url = ""
    actors = []
    ratings = []

    def __init__(self, title, director, genre, actors, poster_url):
        self.ratings = []
        self.title = title
        self.director = director
        self.genre = genre
        self.actors = actors
        self.poster_url = poster_url

    def print(self):
        """Prints movie information."""
        print("######################")
        print(f'Title: {self.title}')
        print(f'Director: {self.director}')
        print(f'Genre: {self.genre}')
        print('Actors: ',end='')
        for actor in self.actors:
            print(actor, end=', ')
        print("")
        print(f'Post URL: {self.poster_url}')
        if self.ratings: 
            print(f'Rating: {self.calculate_rating()}')
        else:
            print(f'Rating: No rating')
        print("######################")

    def calculate_rating(self):
        if len(self.ratings)>0:
            rating = sum(self.ratings)/len(self.ratings)
        else:
            rating = -1
        return rating