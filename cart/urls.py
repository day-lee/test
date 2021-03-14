from django.urls import path
# from . import views
from .views import *
from django.urls import path
from .views import UserRegisterView

app_name = 'cart'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'), #bc it's detailview need slug or pk

    # path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),

    path('success/', success.as_view(), name='success'),
    # path('curriculum-summary/', CurriculumSummaryView.as_view(), name='curriculum-summary'),
    #path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
]

