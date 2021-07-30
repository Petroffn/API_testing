import pytest
from faker import Faker


@pytest.fixture(scope='session')
def api_key():
    return '123456'


@pytest.fixture(scope='session')
def fake():
    return Faker()
