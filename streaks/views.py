from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from .models import Counter, Quote, Profile, FriendRequest, generate_friend_code   
from django.db.models import Q

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            Profile.objects.create(user=user, friend_code=generate_friend_code())                
            return redirect('login')    
    else:
        form = UserCreationForm()  
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def friends(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'friend_code': generate_friend_code()},
    )
    incoming = FriendRequest.objects.filter(receiver=request.user, accepted=False)
    friendships = FriendRequest.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user),
        accepted=True,
    )
    friend_users = []                     
    for f in friendships:                  
        if f.sender == request.user:      
            friend_users.append(f.receiver)
        else:                             
            friend_users.append(f.sender)
    return render(request, 'streaks/friends.html', {
        'profile': profile,
        'incoming': incoming,
        'friendships': friendships,
        'friend_users': friend_users,
    })
    
@login_required
def send_request(request):
    if request.method == 'POST':
        code = request.POST['friend_code']
        profile = Profile.objects.filter(friend_code=code).first()
        if profile and profile.user != request.user:
            FriendRequest.objects.create(sender=request.user, receiver=profile.user)
    return redirect('friends')

@login_required
def accept_request(request, request_id):
    if request.method == 'POST':
        friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user)
        friend_request.accepted = True
        friend_request.save()
    return redirect('friends')