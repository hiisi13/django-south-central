#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_south_central
------------

Tests for `south_central` migration module.
"""

import os
import shutil
import unittest

from south_central import migration


class Test_Migrations(unittest.TestCase):

    test_app_name = 'test_app'


    @classmethod
    def setUpClass(cls):
        cls.migrations = migration.Migrations(cls.test_app_name)
        cls.migrations_dir = cls.test_app_name + '/appmigrations'


    def test_migrations_module(self):
        self.assertEqual(self.test_app_name + '.appmigrations', self.migrations.migrations_module())


    def test_ensure_migrations_dir(self):
        self.assertTrue(os.path.exists(self.migrations_dir))


    def test_ensure_init_file(self):
        init_path = os.path.join(self.migrations_dir, '__init__.py')
        self.assertTrue(os.path.exists(init_path))

    def test_next_filename(self):
        next_filename = self.migrations.next_filename('test')
        self.assertEqual('0001_test.py', next_filename)
