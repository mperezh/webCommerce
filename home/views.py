from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
        )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('home/search.html', {
        "results": results,
        "query": query
    })


def contact(request):
    form = ContactForm()
    return render_to_response('home/contact.html', {'form': form})