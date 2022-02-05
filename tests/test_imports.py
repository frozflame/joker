#!/usr/bin/env python3
# coding: utf-8


import importlib

from volkanic.introspect import find_all_plain_modules

from joker.meta import JokerInterface

ji = JokerInterface()


def test_module_imports():
    for dotpath in find_all_plain_modules(ji.under_project_dir()):
        if dotpath.startswith('joker.'):
            print(dotpath)
            importlib.import_module(dotpath)


if __name__ == '__main__':
    test_module_imports()
