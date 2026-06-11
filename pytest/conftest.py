import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def auth_token(base_url):
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200

    json_data = response.json()

    assert "token" in json_data
    assert json_data["token"] is not None

    return json_data["token"]


@pytest.fixture(scope="module")
def test_create_booking(base_url, auth_token):
    payload = {
        "firstname" : "Jim-carry",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(f"{base_url}/booking", json=payload)
    json_data = response.json()
    assert response.status_code == 200
    print(json_data)
    assert "bookingid" in json_data
    return json_data["bookingid"]
