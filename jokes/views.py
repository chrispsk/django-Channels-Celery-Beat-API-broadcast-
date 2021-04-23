from django.shortcuts import render
from .tasks import get_joke

def index(request):
    # here I can receive jokes even after the page finished loading !!!!! WOW !!!!
    return render(request, "index.html")
