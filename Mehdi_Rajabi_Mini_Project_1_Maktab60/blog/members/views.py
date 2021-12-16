from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, CustomPasswordChangeForm

# Create your views here.


class UserRegisterationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def get_object(self):
        return self.request.user


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_success')
    login_url = 'login'


def password_change_success(request):
    return render(request, 'registration/password_success.html', {})
