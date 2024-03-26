from ninja import NinjaAPI
from api.movie import router as movie_router

api = NinjaAPI()

api.add_router("movies/", movie_router)