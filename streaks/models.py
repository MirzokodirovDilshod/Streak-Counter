from django.db import models

class Counter(models.Model):
    title = models.CharField(max_length = 300)
    current_streak = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    last_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title