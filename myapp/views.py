from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def index(req: WSGIRequest):
    return render(req, 'index.html')