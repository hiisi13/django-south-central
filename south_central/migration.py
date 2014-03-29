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


    def migrations_dir(self):
        module_path = self.migrations_module()
        try:
            module = importlib.import_module(module_path)
        except ImportError:
            try:
                parent = importlib.import_module(".".join(module_path.split(".")[:-1]))
            except ImportError:
                raise
            else:
                return os.path.join(os.path.dirname(parent.__file__), module_path.split(".")[-1])
        else:
            return os.path.dirname(module.__file__)


    def _ensure_migrations_dir(self, app_name):
        migrations_dir = self.migrations_dir()
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




