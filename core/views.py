from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, 'core/homepage.html')