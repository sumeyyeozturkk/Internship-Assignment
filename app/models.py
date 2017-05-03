# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import *

class Kitap(Document):
    name = StringField(required=True)
    sayfa_sayisi = IntField(default=0)
    yazar_adi = StringField(required=True)

def __unicode__(self):
    return self.name


