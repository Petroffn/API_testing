import allure


from src.assertions.base_assertion import Assertion


class ContainsAssertion(Assertion):
    def __init__(self, expected=None):
        super().__init__(expected)
        self.matcher = 'parameter'

    def match(self):
        if self.matcher == 'parameter':
            with allure.step(f'Check that parameter "{self.json_path}" contains "{self.expected}"'):
                assert self.expected in self.actual, self._assert_message('Values is not contain value')

        elif self.matcher == 'json':
            with allure.step(f'Compare json "{self.actual}" contains "{self.expected}"'):
                self._compare_json(self.actual, self.expected)

        elif self.matcher == 'only':
            with allure.step(f'Check that "{self.actual}" contains only "{self.expected}"'):
                assert len(self.actual), self._assert_message('There are no items to compare')

                if isinstance(self.expected, str) or isinstance(self.expected, int):
                    for item in self.actual:
                        assert item == self.expected, self._assert_message('Values is contain wrong value')

                if isinstance(self.expected, list):
                    values = self.actual.copy()
                    for i in reversed(range(len(values))):
                        if values[i] in self.expected:
                            del values[i]
                        assert not len(values), self._assert_message(f'Values is contain wrong value {values}')


class NotContainAssertion(Assertion):
    def __init__(self, expected):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that parameter "{self.json_path}" is not contain "{self.expected}"'):
            assert self.expected not in self.actual, self._assert_message('Values contain value')


class EqualsToAssertion(Assertion):
    def __init__(self, expected=None):
        super().__init__(expected)
        self.matcher = 'parameter'

    def match(self):
        if self.matcher == 'parameter':
            with allure.step(f'Check that parameter "{self.json_path}" equal to "{self.expected}"'):
                assert self.actual == self.expected, self._assert_message('Values is not equal')
        elif self.matcher == 'json':
            with allure.step(f'Compare json "{self.actual}" equals to"{self.expected}"'):
                self._compare_json(self.actual, self.expected)
                self._compare_json(self.expected, self.actual)


class NotEqualToAssertion(Assertion):
    def __init__(self, expected):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that parameter\'s value "{self.json_path}" is not equal to "{self.expected}"'):
            assert self.actual != self.expected, self._assert_message('Values is equal')


class HasLengthAssertion(Assertion):
    def __init__(self, expected=0):
        super().__init__(expected)
        self.matcher = 'same'

    def match(self):
        if self.matcher == 'same':
            with allure.step(f'Check that parameter "{self.json_path}" has length "{self.expected}"'):
                assert len(self.actual) == self.expected, self._assert_message(
                    f'Parameter has wrong length <{len(self.actual)}>')

        elif self.matcher == 'less':
            with allure.step(f'Check that parameter "{self.json_path}" has length less than "{self.expected}"'):
                assert len(self.actual) < self.expected, self._assert_message(
                    f'Parameter has wrong length <{len(self.actual)}> greater then expected')

        elif self.matcher == 'greater':
            with allure.step(f'Check that parameter "{self.json_path}" has length greater than "{self.expected}"'):
                assert len(self.actual) > self.expected, self._assert_message(
                    f'Parameter has wrong length <{len(self.actual)}> less then expected')


class GreaterThanAssertion(Assertion):
    def __init__(self, expected):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that parameter "{self.json_path}" greater than "{self.expected}"'):
            assert self.actual > self.expected, self._assert_message('Value less that expected')


class LessThanAssertion(Assertion):
    def __init__(self, expected):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that parameter "{self.json_path}" less than "{self.expected}"'):
            assert self.actual < self.expected, self._assert_message('Value greater that expected')


class IsEmptyAssertion(Assertion):
    def __init__(self, expected='Is not empty'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is empty'):
            assert not self.actual, self._assert_message('Parameter is not empty')


class IsNotEmptyAssertion(Assertion):
    def __init__(self, expected='Is empty'):
        super().__init__(expected)

    def match(self):
        with allure.step(f'Check that field "{self.json_path}" is not empty'):
            assert self.actual, self._assert_message('Parameter is not empty')


contains = ContainsAssertion
not_contain = NotContainAssertion
equals_to = EqualsToAssertion
not_equal_to = NotEqualToAssertion
has_length = HasLengthAssertion
greater_than = GreaterThanAssertion
less_than = LessThanAssertion
is_not_empty = IsNotEmptyAssertion
is_empty = IsEmptyAssertion
