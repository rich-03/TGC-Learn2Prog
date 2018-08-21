movielist = []
rating = 1.0
while rating >= 0.0:
    title = input("Enter the movie title:")
    genre = input("What is the genre of this movie?")
    rating = float(input("How do you rate the movie?"))
    if rating >= 0.0:
        movie = Movie(title, genre, rating)
        movielist.append(movie)
