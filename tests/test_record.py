import json


def test_response(app, db, client):
    response = client.post('/records/', data=json.dumps({"title": "necooo"}), content_type='application/json')
    assert response.status_code == 201

    url = "https://localhost:5000/records/kch"
    response = client.post(url)
    print("res" + str(response))
    assert response.status_code == 200