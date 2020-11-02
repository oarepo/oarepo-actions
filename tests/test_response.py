import json
from collections import namedtuple

from invenio_accounts.models import Role, User

TestUsers = namedtuple('TestUsers', ['u1', 'u2', 'u3', 'r1', 'r2'])


def test_response(app, db, client):
    response = client.post('/records/', data=json.dumps({"title": "necooo"}), content_type='application/json')
    assert response.status_code == 201

    url = "https://localhost:5000/records/jej"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/blah"
    response = client.get(url)
    assert response.status_code == 401

    url = "https://localhost:5000/records/blah1"
    response = client.get(url)
    assert response.status_code == 404

    url = "https://localhost:5000/records/1/blah"
    response = client.get(url)
    assert response.status_code == 200

    """Returns named tuple (u1, u2, u3, r1, r2)."""
    with db.session.begin_nested():
         r1 = Role(name='role1')
         r2 = Role(name='role2')

         u1 = User(id=1, email='1@test.com', active=True, roles=[r1])
         u2 = User(id=2, email='2@test.com', active=True, roles=[r1, r2])
         u3 = User(id=3, email='3@test.com', active=True, roles=[r2])

         db.session.add(u1)
         db.session.add(u2)
         db.session.add(u3)

         db.session.add(r1)
         db.session.add(r2)

    url = "https://localhost:5000/test/login/1"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/blah"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/test/40"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/test"
    response = client.post(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/test"
    response = client.post(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/test"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/1/blahx"
    response = client.post(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/1/b"
    response = client.get(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/1/b"
    response = client.post(url)
    assert response.status_code == 200

    url = "https://localhost:5000/records/1/b"
    response = client.delete(url)
    assert response.status_code == 200
    #
    url = "https://localhost:5000/records/1/b"
    response = client.put(url)
    assert response.status_code == 200