import pytest

from ..server import server as flask_server


@pytest.fixture
def server():
    yield flask_server


@pytest.fixture
def client(server):
	server.testing = True
	return server.test_client()