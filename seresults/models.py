# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as __

# Create your models here.

SE_GOOGLE = 1
SE_BING = 2


def search_engine_options():
    return [
        (SE_GOOGLE, _(u"Google")),
        (SE_BING, _(u"Bing"))
    ]


STATUS_NEW = 1
STATUS_FINISHED = 2


def status_options():
    return [
        (STATUS_NEW, _(u"Nowe")),
        (STATUS_FINISHED, _(u"Zakończone"))
    ]


class SearchRequest(models.Model):
    query = models.CharField(max_length=255, verbose_name=_(u"Zapytanie"))
    search_engine = models.IntegerField(verbose_name=_(u"Wyszukiwarka"))
    status = models.IntegerField(verbose_name=_(u"Status"), default="1")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Użytkownik"), related_name="search_requests")

    def search_engine_name(self):
        return [n for (i, n) in search_engine_options()
                if i == self.search_engine][0]
    search_engine_name.short_description = _(u"Wyszukiwarka")

    def status_name(self):
        return [n for (i, n) in status_options()
                if i == self.status][0]
    status_name.short_description = _(u"Status")

    def is_finished(self):
        return self.status == STATUS_FINISHED

    def __str__(self):
        return self.query

class SearchResult(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u"Tytuł"))
    url = models.CharField(max_length=255, verbose_name=_(u"URL"))
    description = models.TextField(verbose_name=_(u"Opis"))
    request = models.ForeignKey(SearchRequest, verbose_name=_(u"Zapytanie"), related_name="results")
