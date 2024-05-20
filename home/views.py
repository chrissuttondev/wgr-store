from django.shortcuts import render # noqa


# Create your views here.
def index(request):
    """ view returns index.html """

    return render(request, 'home/index.html')
