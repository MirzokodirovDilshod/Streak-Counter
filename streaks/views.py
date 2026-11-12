from django.shortcuts import render, get_object_or_404, redirect
from .models import Counter, Quote

def home(request):
    counters = Counter.objects.all()
    quote = Quote.objects.order_by('?').first()
    # 1) "name = 'home'" qatorini o'chirdim: manzilga nom berish views.py da emas,
    #    urls.py dagi path() ichida (name='home') qilinadi.
    return render(request, 'streaks/home.html', {'counters': counters, 'quote': quote})

def done(request, counter_id):
    counter = get_object_or_404(Counter, id=counter_id)
    counter.mark_done()
    return redirect('home')