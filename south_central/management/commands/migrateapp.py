from django.core.management.base import BaseCommand
from django.utils import importlib

from south_central.migration import Migrations
from south_central.models import MigrationHistory


def to_apply(all_migrations, applied):
    return [m for m in all_migrations if not m in applied]


def migration_module(basename, module_name):
    return '.'.join([basename, module_name])


def import_migration_module(migrations_module, migration):
    module = migration_module(migrations_module, migration)
    return __import__(module, {}, {}, ['Migration'])


class Command(BaseCommand):

    def handle(self, app, *args, **kwargs):
        app_migrations = Migrations(app)
        migrations_module = app_migrations.migrations_module()

        applied = MigrationHistory.objects.filter(app_name=app) \
                    .values_list('migration_name', flat=True).order_by('applied_on')
        workplan = to_apply(app_migrations, applied)

        for m in workplan:
            module = import_migration_module(migrations_module, m)
            module.Migration().apply()
            MigrationHistory.objects.create(app_name=app, migration_name=m)
