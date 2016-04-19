from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def my_requests(request):
    requests_all = request.user.search_requests.all()

    context = {
        'requests': requests_all
    }

    return render(request, 'results/my_results.html', context)
