from django.shortcuts import render
from .models import Counter, Quote

def home(request):
    counters = Counter.objects.all()
    quote = Quote.objects.order_by('?').first()
    return render(request, 'streaks/home.html', {'counters': counters, 'quote': quote})