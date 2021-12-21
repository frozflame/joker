#!/usr/bin/env python3
# coding: utf-8

import os.path
import urllib.parse
from typing import Generator

from joker.filesys.utils import (
    read_as_chunks, checksum_hexdigest,
    b64_encode_local_file,
)


class Directory:
    def __init__(self, base_dir: str):
        self.base_dir = os.path.abspath(base_dir)

    def __repr__(self):
        cn = self.__class__.__name__
        return '{}({})'.format(cn, repr(self.base_dir))

    def under(self, *paths):
        return os.path.join(self.base_dir, *paths)

    def relative_to_base_dir(self, path: str):
        path = os.path.abspath(path)
        return os.path.relpath(path, self.base_dir)

    under_base_dir = under

    def read_as_chunks(self, path: str, length=-1, offset=0, chunksize=65536) \
            -> Generator[bytes, None, None]:
        path = self.under_base_dir(path)
        return read_as_chunks(
            path, length=length,
            offset=offset, chunksize=chunksize,
        )

    def checksum_hexdigest(self, path: str, algo='sha1') -> str:
        path = self.under_base_dir(path)
        return checksum_hexdigest(path, algo=algo)

    def read_as_binary(self, path: str):
        path = self.under_base_dir(path)
        with open(path, 'rb') as fin:
            return fin.read()

    def read_as_base64_data_url(self, path: str):
        path = self.under_base_dir(path)
        return b64_encode_local_file(path)

    def save_as_file(self, path: str, chunks):
        path = self.under_base_dir(path)
        with open(path, 'wb') as fout:
            for chunk in chunks:
                fout.write(chunk)


class MappedDirectory(Directory):
    def __init__(self, base_dir: str, base_url: str):
        super().__init__(base_dir)
        # Note:
        # urllib.parse.urljoin('/a/b', 'c.jpg') => '/a/c.jpg'
        # urllib.parse.urljoin('/a/b/', 'c.jpg') => '/a/b/c.jpg'
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url

    def relative_to_base_url(self, url: str):
        base_url_path = urllib.parse.urlparse(self.base_url).path
        url_path = urllib.parse.urlparse(url).path
        return os.path.relpath(url_path, base_url_path)


DirectoryInterface = Directory
FileStorageInterface = Directory

__all__ = [
    'DirectoryInterface',
]
