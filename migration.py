import os
import sys

from django.utils import importlib


class Migrations(list):

    def __init__(self, app_name):
        self._app_name = app_name
        migrations_dir = self._ensure_migrations_dir(app_name)
        self._load_migrations(migrations_dir)


    def migrations_module(self):
        return self._app_name + '.appmigrations'


    def _ensure_migrations_dir(self, app_name):
        migrations_dir = self.migration_module()
        if not os.path.isdir(migrations_dir):
            os.mkdir(migrations_dir)
        init_path = os.path.join(migrations_dir, "__init__.py")

        if not os.path.isfile(init_path):
            open(init_path, "w").close()
        return migrations_dir


    def _load_migrations(self, migrations_dir):
        filenames = []
        for f in os.listdir(migrations_dir):
            if os.path.isfile(f) and f.endwith('.py'):
                filenames.append(f)
        self.extend(filenames)




