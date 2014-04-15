from __future__ import print_function

import re
import os
import sys

from django.core.management.base import BaseCommand
from django.db import models
from django.core.exceptions import ImproperlyConfigured

from south_central.migration import Migrations


class Command(BaseCommand):

    def handle(self, app, name, *args, **kwargs):
        if re.search('[^_\w]', name) and name != '-':
            self.error('Migration names should contain only alphanumeric characters and underscores.')

        try:
            models.get_app(app)
        except ImproperlyConfigured:
            self.error("There is no enabled application matching '%s'." % app)

        migrations = Migrations(app)
        new_filename = migrations.next_filename(name)

        with open(os.path.join(migrations.migrations_dir(), new_filename), "w") as fp:
            if args:
                args = join_args(args)
                fp.write(CALL_COMMAND_MIGRATION_TEMPLATE.format(args))
            else:
                fp.write(MIGRATION_TEMPLATE)

    def error(self, message, code=1):
        print(message, file=sys.stderr)
        sys.exit(code)


def join_args(args):
    args = ['"{0}"'.format(arg) if isinstance(arg, str) else str(arg) for arg in args]
    return ", ".join(args)


MIGRATION_TEMPLATE = """# -*- coding: utf-8 -*-


class Migration(object):

    def apply(self):
        pass"""


CALL_COMMAND_MIGRATION_TEMPLATE = """# -*- coding: utf-8 -*-

from django.core.management import call_command


class Migration(object):

    def apply(self):
        call_command({0})"""
