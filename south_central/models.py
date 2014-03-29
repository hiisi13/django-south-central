# -*- coding: utf-8 -*-

from django.db import models
import datetime


class MigrationHistory(models.Model):

    app_name = models.CharField(max_length=255)
    migration_name = models.CharField(max_length=255)
    applied_on = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return "<%s: %s>" % (self.app_name, self.migration_name)
