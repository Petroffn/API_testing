from src.services.base_service import ApiService


class UserApiService(ApiService):
    def __init__(self, api_key):
        super().__init__()
        self._headers.update({'api_key': api_key})

    def create_user(self, body, **kwargs):
        _path = '/user'
        return self._send_post(path=_path, headers=self._headers, payload=body, **kwargs)

    def get_user(self, user_name, **kwargs):
        _path = f'/user/{user_name}'
        return self._send_get(path=_path, headers=self._headers, **kwargs)

    def update_user(self, user_name, body, **kwargs):
        _path = f'/user/{user_name}'
        return self._send_put(path=_path, headers=self._headers, payload=body, **kwargs)

    def delete_user(self, user_name, **kwargs):
        _path = f'/user/{user_name}'
        return self._send_delete(path=_path, headers=self._headers, **kwargs)
