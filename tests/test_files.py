#!/usr/bin/env python3
# coding: utf-8

from joker.interfaces.files import Directory, MappedDirectory


def assert_equal(a, b):
    assert a == b, (a, b)


def test_dir():
    d = Directory('/data/www/files')
    assert_equal(
        d.relative_to_base_dir('/data/www/files/js/v.js'),
        'js/v.js',
    )


def test_mapped_dir():
    md = MappedDirectory(
        '/data/www/files',
        'http://localhost/files'
    )
    assert_equal(
        md.join_url('img/1.jpg'),
        'http://localhost/files/img/1.jpg'
    )
    assert_equal(
        md.convert_local_path_to_url('/data/www/files/js/v.js'),
        'http://localhost/files/js/v.js',
    )
    assert_equal(
        md.convert_url_to_local_path('http://localhost/files/js/v.js'),
        '/data/www/files/js/v.js',
    )
