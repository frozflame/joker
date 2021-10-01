#!/usr/bin/env python3
# coding: utf-8

import os

import volkanic
from volkanic import utils
from volkanic.compat import cached_property


class GlobalInterface(volkanic.GlobalInterface):
    package_name = 'joker.environ'
    default_config = {}
    _meta = {}

    # this method will be moved to JokerInterface at ver 0.3.0
    @classmethod
    def under_joker_dir(cls, *paths):
        path = os.environ.get('JOKER_HOME', cls.under_home_dir('.joker'))
        if not cls._meta.get('joker_dir_made'):
            os.makedirs(path, int('700', 8), exist_ok=True)
            cls._meta['joker_dir_made'] = True
        return os.path.join(path, *paths)

    def under_data_dir(self, *paths, mkdirs=False) -> str:
        dirpath = self.conf['data_dir']
        if not mkdirs:
            return utils.abs_path_join(dirpath, *paths)
        return utils.abs_path_join_and_mkdirs(dirpath, *paths)

    def under_resources_dir(self, *paths) -> str:
        dirpath = self.conf.get('resources_dir')
        if not dirpath:
            dirpath = self.under_project_dir('resources')
        if not dirpath or not os.path.isdir(dirpath):
            raise NotADirectoryError(dirpath)
        return utils.abs_path_join(dirpath, *paths)

    def under_temp_dir(self, ext=''):
        name = os.urandom(17).hex() + ext
        return self.under_data_dir('tmp', name, mkdirs=True)

    # both will be removed
    get_temp_path = under_temp_dir
    under_temp_path = under_temp_dir
    _get_conf_search_paths = None

    @cached_property
    def jinja2_env(self):
        # noinspection PyPackageRequirements
        from jinja2 import Environment, PackageLoader, select_autoescape
        return Environment(
            loader=PackageLoader(self.package_name, 'templates'),
            autoescape=select_autoescape(['html', 'xml']),
        )
