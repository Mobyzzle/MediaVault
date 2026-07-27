import requests
from urllib.parse import urlsplit
import tempfile
import os
from test_link import link,random_link,random_unsafe_link
from pathlib import Path
import logging
from typing import BinaryIO

logger = logging.getLogger(__name__)
#   Structure: validate url -> Request -> check headers -> stream into Temporary file -> Pillow(Processor) validates -> Save into Images Directory -> File ingestion Pipeline
#
#
#

class Downloader:

    def __init__(self):
        self.TEMP_FILE_DIRECTORY = "temp/"
        self.OUTPUT_DIRECTORY = "images/"
        self.MAX_FILE_SIZE_MB = 10
        self.MAX_FILE_SIZE = self.MAX_FILE_SIZE_MB * 1024 * 1024 # 10 MiB
        self.CHUNK_SIZE = 8192
        self.CHUNK_SIZE = 64 * 1024

        self.ALLOWED_FILE_FORMATS = ["image/jpeg","image/png","image/webp","image/jpg"]

        self.TIME_OUT_CONFIG  = (3.0,5.0)
        

    def download(self,source_url:str):
        self._validate_url(source_url=source_url)  # <-- check if URL is in HTTPS format
        return self._create_temp_file(source_url=source_url)


    def _create_temp_file(self, source_url:str) -> BinaryIO:
        
        with requests.get(source_url,timeout=self.TIME_OUT_CONFIG,stream=True,allow_redirects=False) as response:

            

            if response.status_code != 200:
                raise ConnectionError(f"Error with code: {response.status_code}")

            self._check_headers(response)

            temp = self._stream_into_temp_file(response)
                
            return temp
        

    def _validate_url(self,source_url:str) -> None:
        parsed = urlsplit(url=source_url)
        logger.debug(parsed)


        if parsed.scheme != ("https"):
            raise ValueError("Only HTTPS URLs are allowed-")
        if parsed.hostname is None:
            raise ValueError("URL must contain a hostname.")
        if parsed.username or parsed.password:
            raise ValueError("Credentials in URLs are not allowed.")


    def _stream_into_temp_file(self,data:requests.Response) -> BinaryIO:
        downloaded_data = tempfile.NamedTemporaryFile(dir=self.TEMP_FILE_DIRECTORY,delete_on_close=False,delete=True)

        logger.debug(f"Created temp file: {downloaded_data.name}")

        for chunk in data.iter_content(self.CHUNK_SIZE):
            downloaded_data.write(chunk)
            if os.stat(downloaded_data.name).st_size > self.MAX_FILE_SIZE:
                raise ValueError(f"File is too large. Maximum allowed filesize {self.MAX_FILE_SIZE_MB} MB")
        
        logger.debug(f"Returning: {downloaded_data.name}")
        return downloaded_data
        
        


    def _check_headers(self,response:requests.Response) -> None:
        if not response.headers["content-type"] in self.ALLOWED_FILE_FORMATS:
            raise ValueError(f"Unsupported File type, currently supported types:{self.ALLOWED_FILE_FORMATS}")
        if int(response.headers["content-length"]) > self.MAX_FILE_SIZE:
            raise ValueError(f"File is too large. Maximum allowed filesize{self.MAX_FILE_SIZE_MB} MB")
        








if __name__ == "__main__":

    dl = Downloader()
    dl.create_temp_file(link)


