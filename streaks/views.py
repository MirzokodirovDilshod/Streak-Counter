from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Counter, Quote

@login_required
def home(request):
    counters = Counter.objects.filter(owner=request.user)
    quote = Quote.objects.order_by('?').first()
    return render(request, 'streaks/home.html', {'counters': counters, 'quote': quote})

@login_required
def done(request, counter_id):
    counter = get_object_or_404(Counter, id=counter_id, owner=request.user)
    counter.mark_done()
    return redirect('home')

@login_required
def add_counter(request):
    if request.method == 'POST':
        title = request.POST['title']
        Counter.objects.create(title=title, owner=request.user)
    return redirect('home')