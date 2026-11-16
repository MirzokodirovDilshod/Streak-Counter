from django.contrib import admin
from .models import Counter,Quote,Profile,FriendRequest
# Register your models here.
admin.site.register(Counter)
admin.site.register(Quote)
admin.site.register(Profile)
admin.site.register(FriendRequest)
