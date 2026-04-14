from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserLoginForm, ProfileEditForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        self.send_welcome_email(user.email)
        return response

    @staticmethod
    def send_welcome_email(user_email):
        subject = 'Добро пожаловать!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject=subject, message=message, from_email=None, recipient_list=recipient_list)


class CustomLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user

