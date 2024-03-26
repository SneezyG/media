from .models import Movie
from ninja import ModelSchema


class MovieIn(ModelSchema):
    class Meta:
        model = Movie
        exclude = ["id",]
