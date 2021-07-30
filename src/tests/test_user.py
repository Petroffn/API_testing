import random

import allure
import pytest

from src.models.user_model import UserModel
from src.assertions.data_assertion import equals_to
from src.assertions.type_assertion import is_integer
from src.services.user_service import UserApiService


@pytest.fixture(scope='function')
def user(fake):
    _user = UserModel()
    _user.username = fake.user_name()
    _user.firstName = fake.first_name()
    _user.lastName = fake.last_name()
    _user.email = fake.safe_email()
    _user.password = '123456'
    _user.phone = fake.phone_number()
    _user.userStatus = random.randint(1, 5)
    return _user


def test_create_read_user(api_key, user):
    with allure.step('Create user'):
        response = UserApiService(api_key).create_user(user)
        response.status_code_is(200)

    with allure.step('Get user'):
        # Act
        response = UserApiService(api_key).get_user(user.username)
        # Assertion
        response \
            .status_code_is(200) \
            .parameter('$[id]', is_integer()) \
            .parameter('$[username]', equals_to(user.username)) \
            .parameter('$[firstName]', equals_to(user.firstName)) \
            .parameter('$[lastName]', equals_to(user.lastName)) \
            .parameter('$[email]', equals_to(user.email)) \
            .parameter('$[password]', equals_to(user.password)) \
            .parameter('$[phone]', equals_to(user.phone)) \
            .parameter('$[userStatus]', equals_to(user.userStatus))
