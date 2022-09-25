from django.shortcuts import render
from django.http import HttpResponse
from . import github_api
from users.forms import SearchForm
# Create your views here.

def index(request):
    form = SearchForm()

    return render(request, 'index.html', {"form": form})