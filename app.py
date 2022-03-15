from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

movie_repository_singleton.create_movie("This Hill", "Edward", 5.0)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    all_movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, all_movies = all_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    movie_repository_singleton.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

@app.route('/movies/display', methods=['POST','GET'])
def display_movies():
    movie_name = request.form.get('movie_name')
    title=""
    rating=0
    finding_movie = movie_repository_singleton.get_movie_by_title(movie_name)
    if(request.method=='POST'):
        if(finding_movie==None):
            title = "Movie is not Found"
            rating = "There is no rating"
        else:
            title = finding_movie.title
            rating = finding_movie.rating
    return render_template('display_rating.html', title=title, rating=rating,)