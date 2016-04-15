from django.shortcuts import render

# Create your views here.


def my_requests(request):

    requests_all = request.user.search_requests.all()

    context = {
        'requests': request
    }

    return render(request, 'results/my_results.html', context)
