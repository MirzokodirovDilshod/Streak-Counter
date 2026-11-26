from django.db import models
from django.contrib.auth.models import User   # Django'ning tayyor foydalanuvchi modeli
from datetime import date, timedelta
import random 
import string

def generate_friend_code():
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(10))

class Counter(models.Model):
    title = models.CharField(max_length=300)
    current_streak = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    last_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    @property
    def display_streak(self):     
        if self.last_date is None:
            return 0              
        yesterday = date.today() - timedelta(days=1)
        if self.last_date >= yesterday:     
            return self.current_streak
        return 0                    
    @property
    def is_done_today(self):
        return self.last_date == date.today()
    def __str__(self):
        return self.title
    def mark_done(self):
        today = date.today()
        yesterday = today - timedelta(days=1)
        if self.last_date == today:
            return
        if self.last_date == yesterday:
            self.current_streak = self.current_streak + 1
        else:
            self.current_streak = 1
        if self.current_streak > self.best_streak:
            self.best_streak = self.current_streak
        self.last_date = today
        self.save()


class Quote(models.Model):
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friend_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} --> {self.receiver.username}"