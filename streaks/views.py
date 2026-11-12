from django.shortcuts import render, get_object_or_404, redirect
from .models import Counter, Quote

def home(request):
    counters = Counter.objects.all()
    quote = Quote.objects.order_by('?').first()
    return render(request, 'streaks/home.html', {'counters': counters, 'quote': quote})

def done(request, counter_id):
    counter = get_object_or_404(Counter, id=counter_id)
    counter.mark_done()
    return redirect('home')

def add_counter(request):
    if request.method == 'POST':
        title = request.POST['title']
        Counter.objects.create(title=title)
    return redirect('home')
