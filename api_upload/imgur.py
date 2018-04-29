import requests
from rest_blog.config import IMGUR_API_ID, IMGUR_API_SECRIT
from .helpers import ImgurClientError

APP_URL = 'https://api.imgur.com/3/'


class ImgurClient(object):
    def __init__(self, client_id, client_secrit):
        self.client_id = client_id
        self.auth = None
        self.client_secrit = client_secrit

    def get_client_id(self):
        return self.client_id

    def get_client_secrit(self):
        return self.client_secrit

    def prepare_headers(self, force_anon=False):
        headers = {}
        if force_anon or self.auth is None:
            if self.client_id is None:
                raise ImgurClientError('Client credentials not found!')
            else:
                headers['Authorization'] = 'Client-ID %s' % self.get_client_id()
        else:
            headers['Authorization'] = 'Bearer %s' % self.auth.get_current_access_token()

        return headers

    def _make_request(self, method, route, data=None, files=None, force_anon=False):
        method = method.lower()
        method_to_call = getattr(requests, method)

        header = self.prepare_headers(force_anon)
        url = APP_URL + route

        if method in ('delete', 'get'):
            response = method_to_call(url, headers=header, params=data, data=data)
        else:
            response = method_to_call(url, headers=header, files=files, data=data)
        # print("res", response.json())
        return response.json()

    def upload(self, files, config=None):
        return self._make_request(method='post', route='image', files=files)


client = ImgurClient(IMGUR_API_ID, IMGUR_API_SECRIT)
