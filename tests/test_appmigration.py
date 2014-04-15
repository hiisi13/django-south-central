#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from django.core.management import call_command


class Test_Appmigration(unittest.TestCase):

    test_app_name = 'test_app'
    test_migration_name = 'test_migration'

    @classmethod
    def setUpClass(cls):
        cls.migrations_dir = cls.test_app_name + '/appmigrations'
        cls.filename = '0001_' + cls.test_migration_name + '.py'

    def tearDown(self):
        os.remove(os.path.join(self.migrations_dir, self.filename))

    def assert_migration_contents(self, expected):
        with open(os.path.join(self.migrations_dir, self.filename)) as f:
            contents = f.read()
            self.assertTrue(expected in contents)

    def test_create_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name)
        path = os.path.join(self.migrations_dir, self.filename)
        self.assertTrue(os.path.exists(path))

    def test_create_call_command_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name, 'cmd_name')
        self.assert_migration_contents('call_command("cmd_name")')

    def test_create_call_command_with_str_arg_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name,
                     'cmd_name', 'cmd_arg')
        self.assert_migration_contents('call_command("cmd_name", "cmd_arg")')

    def test_create_call_command_with_int_arg_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name,
                     'cmd_name', 1)
        self.assert_migration_contents('call_command("cmd_name", 1)')

    def test_create_call_command_with_float_arg_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name,
                     'cmd_name', 1.01)
        self.assert_migration_contents('call_command("cmd_name", 1.01)')

    def test_create_call_command_with_multiple_args_migration(self):
        call_command('appmigration', self.test_app_name, self.test_migration_name,
                     'cmd_name', 'cmd_arg', 1, 1.01)
        self.assert_migration_contents('call_command("cmd_name", "cmd_arg", 1, 1.01)')
