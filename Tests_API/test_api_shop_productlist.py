import requests
import json




URL = 'https://fineartamerica.com'
get_greatingcards_point= '/shop/greeting+cards'
get_iphonecases_point= '/shop/iphone+cases'

response = requests.get(url= URL + get_greatingcards_point)
pass

def test_get_greatingcards():
    point = URL + get_greatingcards_point
    response = requests.get(url=point)
    assert response.status_code == 200



