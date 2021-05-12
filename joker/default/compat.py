#!/usr/bin/env python3
# coding: utf-8

import pkgutil

import pkg_resources


def get_joker_packages():
    for pkg in pkg_resources.working_set:
        if pkg.project_name.startswith('joker-'):
            yield pkg
        if pkg.project_name == 'joker':
            yield pkg


def get_joker_packages2():
    import joker
    # https://stackoverflow.com/a/57873844/2925169
    return list(pkgutil.iter_modules(
        joker.__path__,
        joker.__name__ + "."
    ))


_packages = [
    'joker.default',
    'joker.flasky',
    'joker.studio',
    'joker.broker',
    'joker.cast',
    'joker.scraper',
    'joker.textmanip',
    'joker.minions',
    'joker.masquerade',
    'joker.xopen',
    'joker.stream',
    'joker.pyoneliner',
    'joker.geometry',
]


def _run():
    import os
    import importlib
    for name in _packages:
        try:
            pkg = importlib.import_module(name)
        except ImportError:
            continue
        for path in pkg.__path__:
            if not os.path.isdir(path):
                path = os.path.split(path)[0]
            path = os.path.split(path)[0]
            yield os.path.join(path, '__init__.py')
