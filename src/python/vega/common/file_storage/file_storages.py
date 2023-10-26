# Importing necessary libraries and modules
from typing import *
from abc import ABC, abstractmethod
import dropbox
import os


# Abstract base class for FileStorage
class FileStorage(ABC):

    # Abstract method to get the URL of a file
    @abstractmethod
    def get_url(self, path) -> str:
        pass

    # Abstract method to upload a file
    @abstractmethod
    def upload_file(self, file_path: str, upload_path: Union[str, None] = None):
        pass

    # Method to download a file using wget command in the system shell
    def download(self, path, download_path: Union[str, None] = None):
        url = self.get_url(path)
        command = f"wget --no-verbose \"{url}\""
        if download_path is not None:
            command = f"{command} -O {download_path}"
        os.system(command)


# DropboxClient class that inherits from FileStorage abstract base class
class DropboxClient(FileStorage):

    # Constructor method with token and folder as parameters
    def __init__(self, token, folder):
        self.__client = dropbox.Dropbox(token)
        self.__folder = folder

    # Method to upload a file to Dropbox
    def upload_file(self, file_path: str, upload_path: Union[str, None] = None):
        if upload_path is None:
            upload_path = os.path.join(self.__folder, file_path.split("/")[-1])

        with open(file_path, "rb") as f:
            meta = self.__client.files_upload(f.read(), upload_path, mode=dropbox.files.WriteMode("overwrite"))
            return meta

    # Method to get the sharable URL of a file in Dropbox
    def get_url(self, path) -> str:
        path = os.path.join(self.__folder, path)

        links = self.__client.sharing_list_shared_links(path).links
        if len(links) > 0:
            url = links[0].url
        else:
            url = self.__client.sharing_create_shared_link_with_settings(path).url
        return f"{url.replace('www.dropbox.com', 'dl.dropboxusercontent.com')}&raw=1"
