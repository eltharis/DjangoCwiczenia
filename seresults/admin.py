# coding=utf-8
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from seresults.models import SearchRequest, status_options, search_engine_options


class StatusFilter(admin.SimpleListFilter):
    title = _(u"Status")
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return status_options()

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(status=self.value())


class SearchRequestAdminForm(forms.ModelForm):
    class Meta:
        model = SearchRequest
        fields = ('query', 'search_engine', 'status', 'user')

    def __init__(self, *args, **kwargs):
        super(SearchRequestAdminForm, self).__init__(*args, **kwargs)

        self.fields['search_engine'] = forms.ChoiceField(choices=search_engine_options(), label=_(u"Wyszukiwarka"))
        self.fields['status'] = forms.ChoiceField(choices=status_options(), label=_(u"Status"))


@admin.register(SearchRequest)
class SearchRequestAdmin(admin.ModelAdmin):
    list_display = ('query', 'field_username', 'search_engine_name', 'field_status_name')
    list_filter = (StatusFilter,)
    search_fields = ('query', 'user__username')

    fields = ('query', 'search_engine', 'status', 'user')
    readonly_fields = ('query', 'user')
    form = SearchRequestAdminForm

    def field_username(self, obj):
        return obj.user.username

    field_username.short_description = _(u"Użytkownik")

    def field_status_name(self, obj):
        return obj.status_name()

    field_status_name.short_description = _(u"Status")

    def get_fields(self, request, obj=None):
        if obj is not None and obj.is_finished():
            return ('query', 'search_engine_name', 'status_name', 'user')
        return self.fields


    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.is_finished():
            return ('query', 'search_engine_name', 'status_name', 'user')
        elif obj is not None:
            return ('query', 'user')
        return ()
