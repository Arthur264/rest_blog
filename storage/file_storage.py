from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from api_upload.dropbox_api import client
from django.utils.datastructures import MultiValueDict


@deconstructible
class FileStorage(Storage):
    def _save(self, name, content):
        data = client.upload(name, content)
        return data

    def get_available_name(self, name, max_length=400):
        return name[:max_length]

    def exists(self, name):
        print("exist", name)
        return False

    def url(self, name):
        print("url", name)
        return name
