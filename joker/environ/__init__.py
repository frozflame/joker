#!/usr/bin/env python3
# coding: utf-8
__version__ = '0.2.3!'

import os

import volkanic
from volkanic.compat import cached_property


class GlobalInterface(volkanic.GlobalInterface):
    package_name = 'joker.environ'

    @cached_property
    def _joker_dir(self):
        path = os.environ.get('JOKER_HOME', self.under_home_dir('.joker'))
        os.makedirs(path, int('700', 8), exist_ok=True)
        return path

    def under_joker_dir(self, *paths):
        return os.path.join(self._joker_dir, *paths)


__gi = GlobalInterface()


def under_joker_dir(*paths):
    return __gi.under_joker_dir(*paths)


# deprecated
def make_joker_dir(*paths):
    return under_joker_dir(*paths)
