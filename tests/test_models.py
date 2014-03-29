#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_south_central
------------

Tests for `south_central` models module.
"""

import os
import shutil
import unittest

from south_central import models


class Test_MigrationHistory(unittest.TestCase):

    def test_str(self):
        model = models.MigrationHistory(
            app_name='test_app',
            migration_name='test_migration'
        )
        self.assertEquals('<test_app: test_migration>', str(model))
