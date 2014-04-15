=============================
django-south-central
=============================

.. image:: https://badge.fury.io/py/django-south-central.png
    :target: https://badge.fury.io/py/django-south-central

.. image:: https://travis-ci.org/hiisi13/django-south-central.svg?branch=master
    :target: https://travis-ci.org/hiisi13/django-south-central

.. image:: https://coveralls.io/repos/hiisi13/django-south-central/badge.png?branch=master
    :target: https://coveralls.io/r/hiisi13/django-south-central?branch=master

Run maintenance commands for Django apps in database migrations fashion.

Quickstart
----------

* Install django-south-central::

    pip install south_central

* Create database table for history::

    python manage.py syncdb


Usage
--------

* Generate migration file and update its contents manually::

    python manage.py appmigration app_name migration_name


* Or, generate Django call_command call with specified arguments::

		python manage.py appmigration app_name migration_name cmd_name cmd_arg


* Apply migration::

    python manage.py migrateapp app_name
