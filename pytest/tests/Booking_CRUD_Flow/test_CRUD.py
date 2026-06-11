from wsgiref import headers

import requests

def test_get_bookings(base_url):
    response = requests.get(f"{base_url}/booking")
    json_data = response.json()
    assert response.status_code == 200

def test_get_a_booking(base_url, auth_token):
    response = requests.get(f"{base_url}/booking/2")
    json_data = response.json()
    assert response.status_code == 200
    assert "firstname" and "bookingdates" in json_data

def test_update_booking(test_create_booking, base_url, auth_token):
    payload = {
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }

    headers = {
        "Cookie": f"token={auth_token}",
        "Accept": "application/json"
    }

    response = requests.put(
        f"{base_url}/booking/{test_create_booking}",
        json=payload,
        headers=headers
    )

    json_data = response.json()

    assert response.status_code == 200
    assert json_data["firstname"] == payload["firstname"]
    assert json_data["lastname"] == payload["lastname"]
    assert json_data["totalprice"] == payload["totalprice"]

def test_partial_update_booking(test_create_booking, base_url, auth_token):
    payload = {
        "firstname" : "Adel",
        "lastname" : "Elakour",
    }
    headers = {
        "Cookie": f"token={auth_token}",
        "Accept": "application/json"
    }

    response = requests.patch(
        f"{base_url}/booking/{test_create_booking}",
        json=payload,
        headers=headers
    )

    json_data = response.json()
    assert response.status_code == 200
    assert json_data["firstname"] == payload["firstname"]
    assert json_data["lastname"] == payload["lastname"]

def test_delete_booking(test_create_booking, base_url, auth_token):

    headers = {
        "Cookie": f"token={auth_token}",
        "Accept": "application/json"
    }

    response = requests.delete(
        f"{base_url}/booking/{test_create_booking}",
            headers=headers
    )

    assert response.status_code == 201
    assert response.text == "Created"
