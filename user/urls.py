from django.urls import path
# from . import views
from .views import *
from django.urls import path
from .views import UserRegisterView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
]

