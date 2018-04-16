import dropbox
from django.utils._os import safe_join
from storages.utils import setting

DROPBOX_ROOT_PATH = '/dir/'

class DropBox:
    def __init__(self, root_path=None):
        self.access_token = 'o4rkVfnXj2AAAAAAAAAANqK_8Aglam7dB4RhmDHSSG7UIIYuJZIQZtJAGTsYhe-1'
        self.root_path = root_path or setting('DROPBOX_ROOT_PATH', '/')
        
    def _full_path(self, name):
        if name == '/':
            name = ''
        return safe_join(self.root_path, name).replace('\\', '/')

    def upload(self, name, file):
        dbx = dropbox.Dropbox(self.access_token)
        meta = dbx.files_upload(file.read(), self._full_path(name))
        link = dbx.sharing_create_shared_link(self._full_path(name)).url
        link = link[:-1] + '1'
        return link
            
            
client = DropBox()
