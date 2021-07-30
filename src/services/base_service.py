import json
import logging

import allure
import curlify
import jsonschema
from jsonpath_ng.ext import parse
import requests

from config import BASE_URL


class Attach:
    def _attach_url(self, response):
        _url = response.request.url
        allure.attach(_url, 'Url', attachment_type=allure.attachment_type.TEXT)

    def _attach_headers(self, response):
        _headers = dict(response.request.headers)
        _headers = json.dumps(_headers, indent=3, sort_keys=True)
        allure.attach(_headers, 'Headers', attachment_type=allure.attachment_type.JSON)

    def _attach_payload(self, response):
        _payload = response.request.body.decode("utf-8")
        _payload = json.loads(_payload)
        _payload = json.dumps(_payload, indent=3, sort_keys=True)
        allure.attach(_payload, 'Request to server', attachment_type=allure.attachment_type.JSON)

    def _attach_response(self, response):
        try:
            _response = response.json()
            _response = json.dumps(_response, indent=3, sort_keys=True)
            allure.attach(_response, 'Response from server', attachment_type=allure.attachment_type.JSON)

        except:
            _response = response.text
            allure.attach(_response, 'Response from server', attachment_type=allure.attachment_type.TEXT)

    def _attach_response_time(self, response):
        response_time = response.elapsed.total_seconds()
        response_time = str(response_time)
        allure.attach(response_time, 'Response time', attachment_type=allure.attachment_type.TEXT)

    def _attach_curl(self, response):
        curl = curlify.to_curl(response.request)
        allure.attach(curl, 'Curl', attachment_type=allure.attachment_type.TEXT)


class ApiService(Attach):
    def __init__(self):
        self._headers = {'Content-Type': 'application/json'}
        self._base_url = BASE_URL

    def _url(self, path):
        return self._base_url + path

    def _send_get(self, path, headers, **kwargs):
        with allure.step(f'GET {path}'):
            _response = requests.get(url=self._url(path), headers=headers, **kwargs)
            self._attach_curl(_response)
            self._attach_url(_response)
            self._attach_headers(_response)
            self._attach_response(_response)
            self._attach_response_time(_response)
        return AssertResponse(_response)

    def _send_post(self, path, headers, payload, **kwargs):
        with allure.step(f'POST {path}'):
            _response = requests.post(url=self._url(path), json=payload, headers=headers, **kwargs)
            self._attach_curl(_response)
            self._attach_url(_response)
            self._attach_headers(_response)
            self._attach_payload(_response)
            self._attach_response(_response)
            self._attach_response_time(_response)
        return AssertResponse(_response)

    def _send_put(self, path, headers, payload, **kwargs):
        with allure.step(f'PUT {path}'):
            _response = requests.put(url=self._url(path), json=payload, headers=headers, **kwargs)
            self._attach_curl(_response)
            self._attach_url(_response)
            self._attach_headers(_response)
            self._attach_payload(_response)
            self._attach_response(_response)
            self._attach_response_time(_response)
        return AssertResponse(_response)

    def _send_patch(self, path, headers, payload, **kwargs):
        with allure.step(f'PATCH {path}'):
            _response = requests.patch(url=self._url(path), json=payload, headers=headers, **kwargs)
            self._attach_curl(_response)
            self._attach_url(_response)
            self._attach_headers(_response)
            self._attach_payload(_response)
            self._attach_response(_response)
            self._attach_response_time(_response)
        return AssertResponse(_response)

    def _send_delete(self, path, headers, **kwargs):
        with allure.step(f'DELETE {path}'):
            _response = requests.delete(url=self._url(path), headers=headers, **kwargs)
            self._attach_curl(_response)
            self._attach_url(_response)
            self._attach_headers(_response)
            self._attach_response(_response)
            self._attach_response_time(_response)
        return AssertResponse(_response)


class AssertResponse:
    def __init__(self, response):
        self.response = response
        logging.info(f'\n\t\t'
                     f'{response.request.method} {response.request.url} '
                     f'Status code: {response.status_code}\n\t\t'
                     f'Headers: {response.request.headers}\n\t\t'
                     f'Request: {response.request.body}\n\t\t'
                     f'Response: {response.text}\n\t\t'
                     f'Response time: {response.elapsed.total_seconds()}')

    def status_code_is(self, code):
        with allure.step(f'Check that status code is {code}'):
            actual_status_code = self.response.status_code
            assert actual_status_code == code, f'Actual status code: {actual_status_code}, expected: {code}'
        return self

    def validate_json_schema(self, expected_json_schema):
        with allure.step('Validate json schema'):

            exception = None

            try:
                jsonschema.validate(self.response.json(), expected_json_schema)

            except jsonschema.exceptions.ValidationError as e:

                exception_text = str(e)

                allure.attach(exception_text, 'Validation Error', attachment_type=allure.attachment_type.TEXT)
                allure.attach(json.dumps(expected_json_schema, indent=3), 'Json Schema',
                              attachment_type=allure.attachment_type.JSON)

                exception_text_lines = exception_text.splitlines()
                exception = f'{exception_text_lines[0]}.\n' \
                            f'{exception_text_lines[2]}'

            if exception:
                raise AssertionError(exception)

        return self

    def get_parameter(self, json_path):
        values = [match.value for match in parse(json_path).find(self.response.json())]
        assert len(values), f'Parameter: {json_path} is not found'
        value = values[0]

        return value

    def get_parameters(self, json_path):
        values = [match.value for match in parse(json_path).find(self.response.json())]
        return values

    def parameter(self, json_path, assertion):
        assertion.actual = self.get_parameter(json_path)
        assertion.json_path = json_path
        assertion.match()
        return self

    def parameters(self, json_path, assertion):
        assertion.actual = self.get_parameters(json_path)
        assertion.json_path = json_path
        assertion.match()
        return self

    def json(self):
        return self.response.json()

    @property
    def text(self):
        return self.response.text
