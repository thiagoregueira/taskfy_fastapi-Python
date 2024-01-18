from jose import jwt

from taskfy.security import SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data=data)

    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded_token['test'] == data['test']
    assert decoded_token[
        'exp'
    ]  # Testa se o valor de exp foi adicionado ao token
