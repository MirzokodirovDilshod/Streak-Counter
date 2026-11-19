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
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('friends/add/', views.send_request, name='send_request'),
    path('friends/', views.friends, name='friends'),
    path('friends/accept/<int:request_id>/', views.accept_request,name='accept_request'),
    path('friends/<int:user_id>/', views.friends_profile, name='friends_profile'),
] 