import requests
import json

URL = 'https://petstore.swagger.io/v2/swagger.json'


def test_get_pet_bystatus():
    point = URL + '/pet/findByStatus?status=sold'
    response = requests.get(url=point)
    content = json.loads(response.content)
    assert content['data'].get("id")


def test_delete_pet_byid():
    point = URL + '/pet/76342797'
    apikey= 'special-key'
    response = requests.delete(url=point, headers=apikey)
    assert response.status_code == 200  # according to swagger expected 200, not 204


def test_update_pet_byid():
    point = URL + '/pet'
    body = {
    "id": 1239529653,
    "category": {
      "id": 2495190326,
      "name": "dog"
    },
    "name": "hello kitty",
    "photoUrls": [
      "http://foo.bar.com/1",
      "http://foo.bar.com/2"
    ],
    "tags": [
      {
        "id": 3193795698,
        "name": "blank"
      }
    ],
    "status": "available"
  }
    response = requests.put(url=point, body=body)
    content = json.loads(response.content)
    assert content['data'].get("status")  # initial status value "sold"


def test_create_pet():
    point = URL + '/pet'
    body = {
    "id": 1988,
    "category": {
      "id": 249516,
      "name": "dog"
    },
    "name": "hello doggy",
    "photoUrls": [
      "http://foo.bar.com/1"
    ],
    "tags": [
      {
        "id": 3193698,
        "name": "blank"
      }
    ],
    "status": "available"
  }
    response = requests.post(url=point, body=body)
    content = json.loads(response.content)
    assert content['data'].get("id")