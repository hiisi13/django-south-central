#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import unittest

from django.core.management import call_command

from south_central.models import MigrationHistory


class Test_Migrateapp(unittest.TestCase):

    test_app_name = 'test_app'
    test_migration_name = 'test_migration'

    @classmethod
    def setUpClass(cls):
        cls.migrations_dir = cls.test_app_name + '/appmigrations'
        call_command('appmigration', cls.test_app_name, cls.test_migration_name)
        call_command('migrateapp', cls.test_app_name)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.migrations_dir)

    def test_create_migrationhistory(self):
        migration_name = '0001_' + self.test_migration_name
        self.assertEqual(1, MigrationHistory.objects.count())
        self.assertTrue(
            MigrationHistory.objects.filter(
                app_name=self.test_app_name,
                migration_name=migration_name
            ).exists()
        )

    def test_migration_run_once(self):
        call_command('migrateapp', self.test_app_name)
        self.assertEqual(1, MigrationHistory.objects.count())
