import pytest
from fastapi.testclient import TestClient

from taskfy.app import app


@pytest.fixture
def client():
    return TestClient(app)
