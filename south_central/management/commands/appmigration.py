import re
import os

from django.core.management.base import BaseCommand
from django.db import models
from django.core.exceptions import ImproperlyConfigured

from south_central.migration import Migrations


class Command(BaseCommand):

    def handle(self, app, name, *args, **kwargs):
        if re.search('[^_\w]', name) and name != '-':
            self.error('Migration names should contain only alphanumeric characters and underscores.')

        try:
            app_module = models.get_app(app)
        except ImproperlyConfigured:
            print("There is no enabled application matching '%s'." % app)
            return

        migrations = Migrations(app)
        new_filename = migrations.next_filename(name)

        with open(os.path.join(migrations.migrations_dir(), new_filename), "w") as fp:
            fp.write(MIGRATION_TEMPLATE)


MIGRATION_TEMPLATE = """# -*- coding: utf-8 -*-


class Migration(object):

    def apply(self):
        pass"""
