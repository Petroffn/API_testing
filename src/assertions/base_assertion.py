from abc import ABC, abstractmethod


class BaseAssertion:
    def __init__(self, expected):
        self.matcher = 'less'
        self.json_path = None
        self.actual = None
        self.expected = expected

    def _compare_json(self, actual, expected, parameter=None):
        if type(expected) is list:
            if type(actual) is not list:
                raise TypeError(f'{actual} is not "List"')
            for list_index, list_item in enumerate(expected):
                self._compare_json(actual[list_index], list_item, list_index)
            return

        if type(expected) is dict:
            if type(actual) is not dict:
                raise TypeError(f'{actual} is not "Dist"')
            for dict_key, dict_value in expected.items():
                if dict_key not in actual:
                    raise IndexError(self._assert_message(f'Parameter: "{dict_key}" is not found'))
                else:
                    self._compare_json(actual[dict_key], dict_value, dict_key)
            return

        if str(actual) == str(expected):
            return
        else:
            raise AssertionError(self._assert_message(f'Parameter: "{parameter}" in jsons different'))

    def greater_than(self, expected):
            self.expected = expected
            self.matcher = 'greater'
            return self

    def less_than(self, expected):
        self.expected = expected
        return self

    def json(self, expected):
        self.expected = expected
        self.matcher = 'json'
        return self

    def only(self, expected):
        self.expected = expected
        self.matcher = 'only'
        return self

    def _assert_message(self, param):
        pass


class Assertion(ABC, BaseAssertion):
    @abstractmethod
    def match(self):
        pass
