from ninja.testing import TestClient
from .movie import router as movie_router
from .factories import generate_movie
import json
import pytest


@pytest.mark.django_db
def test_list_movie_endpoint():
   client = TestClient(movie_router)
   response = client.get("/")
   movie_list = response.json()

   assert response.status_code == 200
   assert isinstance(movie_list, list)
   
   
  

@pytest.mark.django_db
def test_add_movie_endpoint():
    
    client = TestClient(movie_router)
    
    payload = generate_movie()
    
    response = client.post(
        "new/", 
        json.dumps(payload),
        content_type='application/json'
    )

    assert response.status_code == 200

    expected_response = {"movie_name": payload["name"]}
    assert response.json() == expected_response
    
    
    