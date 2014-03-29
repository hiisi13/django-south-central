#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import unittest

from django.core.management import call_command


class Test_Appmigration(unittest.TestCase):

    test_app_name = 'test_app'
    test_migration_name = 'test_migration'


    @classmethod
    def setUpClass(cls):
        cls.migrations_dir = cls.test_app_name + '/appmigrations'
        call_command('appmigration', cls.test_app_name, cls.test_migration_name)
        cls.filename = '0001_' + cls.test_migration_name + '.py'


    @classmethod
    def tearDownClass(cls):
        os.remove(os.path.join(cls.migrations_dir, cls.filename))


    def test_create_migration(self):
        path = os.path.join(self.migrations_dir, self.filename)
        self.assertTrue(os.path.exists(path))
