# -*- coding: utf-8 -*-

from django import forms

from seresults.models import SearchRequest, search_engine_options


class SearchRequestForm(forms.ModelForm):
    class Meta:
        model = SearchRequest
        fields = ('query', 'search_engine')

    def __init__(self, *args, **kwargs):
        super(SearchRequestForm, self).__init__(*args, **kwargs)

        self.fields['search_engine'] = forms.ChoiceField(choices=search_engine_options())

    def save(self, user, commit=True):
        obj = super(SearchRequestForm, self).save(commit=False)
        obj.user = user
        obj.save()
        return obj
