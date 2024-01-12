from sqlalchemy import select

from taskfy.models import User


def test_create_user(session):
    new_user = User(
        username='John', email='john@example.com', password='secret'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'John'))

    assert user.username == 'John'
