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
        cls.migrations_dir = cls.test_app_name + 'appmigrations'


    def test_migrations_module(self):
        self.assertEqual(cls.migrations_dir, cls.migrations.migrations_module())


    def test_ensure_migrations_dir(self):
        self.assertTrue(os.path.exists(cls.migrations_dir))


    def test_ensure_init_file(self):
        init_path = os.path.join(cls.migrations_dir, '__init__.py')
        self.assertTrue(os.path.exists(init_path))


    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.test_app_name)
