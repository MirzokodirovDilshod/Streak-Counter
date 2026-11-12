from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from streaks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('done/<int:counter_id>/', views.done, name='done'),
    path('add/', views.add_counter, name='add_counter'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]