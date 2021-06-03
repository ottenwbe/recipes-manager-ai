import os
import tempfile

import pytest

from analyzer import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    """Test /"""

    result = client.get('/')
    assert b'Recipes Analyzer' in result.data


def test_similarity(client):
    """Test /"""

    result = client.get('/')
    assert b'Recipes Analyzer' in result.data
