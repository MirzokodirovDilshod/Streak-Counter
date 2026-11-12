from django.contrib import admin
from django.urls import path
from streaks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('done/<int:counter_id>/', views.done,name='done'),
]