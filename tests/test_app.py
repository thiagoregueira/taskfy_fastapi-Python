def test_read_root(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World!'}


# test_create
def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'John',
            'email': 'john@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'name': 'John',
        'email': 'john@example.com',
    }


# test_read
def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {'id': 1, 'name': 'John', 'email': 'john@example.com'},
        ]
    }


# test_update
def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'name': 'Jane',
            'email': 'jane@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Jane',
        'email': 'jane@example.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/10',
        json={
            'name': 'Jane',
            'email': 'jane@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


# test_delete
def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/10')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
