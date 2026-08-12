from django.urls import path
from . import views




urlpatterns = [
    path('login/', views.authPage, name='login'),
    path('register/', views.authPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    
    path('createroom/', views.createroom, name='create_room'),
    path('deleteroom/<str:pk>/', views.deleteroom, name='delete_room'),
    path('deletemessage/<str:pk>/', views.deletemessage, name='delete_message'),
    path('updateroom/<str:pk>/', views.updateroom, name='update_room'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('updateuser/', views.updateuser, name='update_user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
    
]
