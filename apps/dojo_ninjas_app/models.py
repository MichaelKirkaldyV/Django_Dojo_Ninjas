# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_At = models.DateTimeField(auto_now=True)

class Ninjas(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_At = models.DateTimeField(auto_now=True)
	dojos = models.ForeignKey(Dojos, related_name="ninjas")


