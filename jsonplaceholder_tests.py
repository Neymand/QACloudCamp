import requests

HEADERS = {
    'Content-Type': "application/json; charset=UTF-8"
}


# https://jsonplaceholder.typicode.com API functions
# GET /posts
def jsonplaceholder_get():
    return requests.get('https://jsonplaceholder.typicode.com/posts')


# POST /posts
def jsonplaceholder_post(title, body, userid):
    json = {
        'title': str(title),
        'body': str(body),
        'userId': str(userid)
    }
    return requests.post('https://jsonplaceholder.typicode.com/posts', headers=HEADERS, json=json)


# DELETE /posts
def jsonplaceholder_delete(post_number_for_deletion):
    return requests.delete('https://jsonplaceholder.typicode.com/posts/' + str(post_number_for_deletion))


# API functions tests
# GET /posts
def test_jsonplaceholder_get():
    assert jsonplaceholder_get().status_code == 200


# POST /posts
def test_jsonplaceholder_post():
    assert jsonplaceholder_post("Test title", "Test body", 10).status_code == 201


# DELETE /posts
def test_jsonplaceholder_delete():
    assert jsonplaceholder_delete(100).status_code == 200
