from django.http import HttpResponse
from .models import Counter
# Create your views here.
def home(request):
    counts = Counter.objects.all()
    names = [c.title for c in counts]
    return HttpResponse(",".join(names))
