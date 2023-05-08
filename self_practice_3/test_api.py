import requests
import json

def test_api_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    assert response.status_code == 200

def test_all_dogs_api():
    url = 'https://dog.ceo/api/breeds/list/all'

    response = requests.request("GET", url)
    body = response.json()["message"]
    body_dog = list(body.keys())[0]
    print(body_dog)

    url_2 = f'https://dog.ceo/api/breed/{body_dog}/images'

    response_2 = requests.request("GET", url_2)
    print(response_2)

def test_api_random_cat():
    url_all_cats = 'https://api.thecatapi.com/v1/images/search?limit=100'
    url_my_cat = 'https://api.thecatapi.com/v1/images/search'

    response_all_cats = requests.request("GET", url_all_cats)
    response_my_cat = requests.request("GET", url_my_cat)
    print(response_all_cats.text)

    all_cats_data = json.loads(response_all_cats.text)

    all_cats_ids = [cat_data['id'] for cat_data in all_cats_data]
    my_cat_data = json.loads(response_my_cat.text)

    my_cat_id = my_cat_data[0]['id']

    print(f"All cats ids: {all_cats_ids}")
    print(f"My cat id: {my_cat_id}")
    assert my_cat_id in all_cats_ids

    # assert response_all_cats["id"] == response_my_cat["id"]