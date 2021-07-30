import allure

from src.assertions.base_assertion import Assertion


class IsStringAssertion(Assertion):
    def __init__(self, expected='Is string'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is string'):
            assert isinstance(self.actual, str), self._assert_message('Parameter is not string')

    def _assert_message(self, param):
        pass


class IsIntegerAssertion(Assertion):
    def __init__(self, expected='Is integer'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is number'):
            assert isinstance(self.actual, int), self._assert_message('Parameter is not number')

    def _assert_message(self, param):
        pass


class IsListAssertion(Assertion):
    def __init__(self, expected='Is list'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is list'):
            assert isinstance(self.actual, list), self._assert_message('Parameter is not list')

    def _assert_message(self, param):
        pass


class IsDictAssertion(Assertion):
    def __init__(self, expected='Is dict'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is dict'):
            assert isinstance(self.actual, dict), self._assert_message('Parameter is not dict')

    def _assert_message(self, param):
        pass


class IsBoolAssertion(Assertion):
    def __init__(self, expected='Is boolean'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is boolean'):
            assert isinstance(self.actual, bool), self._assert_message('Parameter is not boolean')

    def _assert_message(self, param):
        pass


is_string = IsStringAssertion
is_integer = IsIntegerAssertion
is_list = IsListAssertion
is_dict = IsDictAssertion
is_bool = IsBoolAssertion
