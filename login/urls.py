
from django.urls import path
from .views import register_user,user_login ,user_logout,Profile

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('Profile/<int:id>', Profile, name='Profile'),
]