from taskfy.schemas import UserPublic


# Testando o token
def test_get_token(client, user):
    response = client.post(
        '/token/',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


# test_create
def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'John',
            'email': 'john@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'John',
        'email': 'john@example.com',
    }


def test_create_user_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'test@example.com',  # already exists in database
            'password': 'test',
        },
    )

    assert response.status_code == 409
    assert response.json() == {'detail': 'Username already exists'}


# test_read
def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


# test_update
def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client, user):
    response = client.put(
        '/users/10',
        json={
            'username': 'Jane',
            'email': 'jane@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


# test_delete
def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_not_found(client, user):
    response = client.delete('/users/10')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
