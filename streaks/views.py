from django.shortcuts import render   
from .models import Counter

def home(request):
    counters = Counter.objects.all()  
    return render(request, 'streaks/home.html', {'counters': counters})