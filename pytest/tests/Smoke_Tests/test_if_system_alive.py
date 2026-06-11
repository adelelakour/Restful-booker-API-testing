import requests

def test_ping(base_url):
    response = requests.get(f"{base_url}/ping")

    assert response.status_code == 201
    assert response.text == "Created"


def test_get_bookings(base_url):
    response = requests.get(f"{base_url}/booking")

    assert response.status_code == 200
