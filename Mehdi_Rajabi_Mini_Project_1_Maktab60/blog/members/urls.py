from django.urls import path
from .views import (
   UserRegisterationView, AccountSettingsView,
   MyPasswordChangeView, password_change_success,
   UserProfileView
)

urlpatterns = [
   path('register/', UserRegisterationView.as_view(), name='register'),
   path(
      'account-settings/',
      AccountSettingsView.as_view(),
      name='account_settings'
   ),
   path(
      'password/',
      MyPasswordChangeView.as_view(),
      name='password_change'
   ),
   path('password-success/', password_change_success, name='password_success'),
   path('<slug:slug>/profile/', UserProfileView.as_view(), name='profile'),
]
