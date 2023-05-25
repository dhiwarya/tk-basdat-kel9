from django.urls import path
from .views import *

app_name = 'landing_page'

urlpatterns = [
    path('',index, name='index'),
    path('auth', login_register, name='login_register'),
    path('auth/login/', login, name='login'),
    path('auth/logout/', logout, name='logout'),
    path('auth/register/', register, name='register'),
]
