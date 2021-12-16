from django.urls import path
from .views import (
   UserRegisterationView, UserEditView,
   MyPasswordChangeView, password_change_success
)

urlpatterns = [
   path('register/', UserRegisterationView.as_view(), name='register'),
   path('edit-profile/', UserEditView.as_view(), name='edit_profile'),
   path(
      'password/',
      MyPasswordChangeView.as_view(),
      name='password_change'
   ),
   path('password-success/', password_change_success, name='password_success')
]
