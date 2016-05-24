# -*- coding: utf-8 -*-

from django import forms

from seresults.models import SearchRequest, search_engine_options
from seresults.tasks import find_results


class SearchRequestForm(forms.ModelForm):
    class Meta:
        model = SearchRequest
        fields = ('query', 'search_engine')

    def __init__(self, *args, **kwargs):
        super(SearchRequestForm, self).__init__(*args, **kwargs)

        self.fields['search_engine'] = forms.ChoiceField(choices=search_engine_options())

    def save(self, user, commit=True):
        search_request = super(SearchRequestForm, self).save(commit=False)
        search_request.user = user
        search_request.save()
        find_results.delay(search_request)
        return search_request
