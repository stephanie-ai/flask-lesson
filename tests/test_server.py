import pytest
import json

def test_homepage(client):
    get_res = client.get("/")
    assert get_res.status_code == 200
    assert "Hello from Flask!" in get_res.get_data(as_text=True)
    post_res = client.post("/")
    assert post_res.status_code != 200

def 


def get_dogs():
    res = client.get("/api/dogs")
    assert res.status_code == 200
    assert "Look at these wonderful dogs" in res.get_data(as_text=True)

