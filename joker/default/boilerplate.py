#!/usr/bin/env python3
# coding: utf-8

import os
from typing import Union


def save(path: str, content: Union[str, bytes]):
    if path.endswith('/'):
        dirpath, path = path, ''
    else:
        dirpath = os.path.split(path)[0]
    os.makedirs(dirpath, exist_ok=True)
    if path:
        mode = 'wb' if isinstance(content, bytes) else 'w'
        with open(path, mode) as fout:
            fout.write(content)


def make_boilerplate_dir(config: dict):
    for path, content in config.items():
        _save(path, content)
