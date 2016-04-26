# coding=utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from seresults.forms import SearchRequestForm

# Create your views here.


@login_required
def my_requests(request):
    requests_all = request.user.search_requests.all()

    context = {
        'requests': requests_all
    }

    return render(request, 'results/my_results.html', context)


@login_required
def add_request(request):
    form = SearchRequestForm()
    if request.method == "POST":
        form = SearchRequestForm(data=request.POST)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, _(u"Zapytanie dodane"))
            return HttpResponseRedirect(redirect_to=reverse('my_request'))
        else:
            messages.error(request, _(u"W formularzu wystąpiły błędy"))

    context = {'form': form}
    return render(request, 'results/add_request.html', context)
