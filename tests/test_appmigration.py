#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import unittest

from django.core.management import call_command
from django.conf import settings

from south_central import migration


class Test_Appmigration(unittest.TestCase):

    test_app_name = 'test_app'
    test_migration_name = 'test_migration'


    @classmethod
    def setUpClass(cls):
        cls.migrations_dir = cls.test_app_name + '/appmigrations'
        call_command('appmigration', cls.test_app_name, cls.test_migration_name)


    def test_create_migration(self):
        filename = '0001_' + self.test_migration_name + '.py'
        path = os.path.join(self.migrations_dir, filename)
        self.assertTrue(os.path.exists(path))


    @classmethod
    def tearDownClass(cls):
        pass
        # shutil.rmtree(cls.test_app_name)
