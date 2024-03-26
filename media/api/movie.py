from ninja import Router
from .models import Movie
from .schema import MovieIn

router = Router()

@router.get('/', description="Get all movies ordered by ranking")
def list_movies(request):
    movies = Movie.objects.all().values()
    return list(movies)
    
    
    
@router.post("new/", description="Create a new movie") 
def add_movie(request, payload: MovieIn):
    payload_dict = payload.dict()
    movie = Movie.objects.create(**payload_dict)
    return {"movie_name": movie.name}


