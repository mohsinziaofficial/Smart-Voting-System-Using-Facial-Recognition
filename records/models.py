# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)

    return wrapper


# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    residence = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=150, null=True)
    occupation = models.CharField(max_length=150, null=True)
    marital_status = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    recorded_at = models.DateTimeField(default=datetime.now, blank=True)
    # image = models.ImageField(upload_to='Vote/static/img/', blank=True)
    image = models.ImageField(upload_to=path_and_rename('Vote/static/img/'), blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Records"
