from django.urls import path
from users.views import register, user_login, reset

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('reset/', reset, name='reset'),
]