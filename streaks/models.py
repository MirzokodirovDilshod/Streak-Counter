from django.db import models
from django.contrib.auth.models import User   # Django'ning tayyor foydalanuvchi modeli
from datetime import date, timedelta

class Counter(models.Model):
    title = models.CharField(max_length=300)
    current_streak = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    last_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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