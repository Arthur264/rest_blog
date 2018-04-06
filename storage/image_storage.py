from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from imgur.client import client
from django.utils.datastructures import MultiValueDict


@deconstructible
class ImageStorage(Storage):
    def _save(self, name, content):
        print("save", name, content)
        data = client.upload(MultiValueDict({"image": [content]}))

        return data['data']['link']

    def get_available_name(self, name, max_length):
        return name[:max_length]

    #
    # def get_valid_name(self, name):
    #     print("valid", name)

    def exists(self, name):
        print("exist", name)
        return False

    def url(self, name):
        print("url", name)
        return name
