# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as __

# Create your models here.

SE_GOOGLE = 1
SE_BING = 2


STATUS_NEW = 1
STATUS_FINISHED = 2


class SearchRequest(models.Model):

    query = models.CharField(max_length=255, verbose_name=_(u"Zapytanie"))
    seaech_engine = models.IntegerField(verbose_name=_(u"Wyszukiwarka"))
    status = models.IntegerField(verbose_name=_(u"Ststus"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Użytkownik"), related_name="search_requests")


class SearchResult(models.Model):

    title = models.CharField(max_length=255, verbose_name=_(u"Tytuł"))
    url = models.CharField(max_length=255, verbose_name=_(u"URL"))
    description = models.TextField(verbose_name=_(u"Opis"))
    request = models.ForeignKey(SearchRequest, verbose_name=_(u"Zapytanie"), related_name="results")
