from time import sleep
from celery import shared_task
from .models import Movie



@shared_task(name="increment_rank")
def increment_rank():
  movies = Movie.objects.filter(status__in=["coming_up", "starting",])
  
  for movie in movies:
    movie.ranking += 1
    movie.save()
