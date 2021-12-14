from django.urls import path
from .views import UserRegisterationView

urlpatterns = [
   path('register/', UserRegisterationView.as_view(), name='register'),
]
