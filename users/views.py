from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        self.send_welcome_email(user.email)
        return response

    @staticmethod
    def send_welcome_email(user_email):
        subject = 'Добро пожаловать!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject=subject, message=message, from_email=None, recipient_list=recipient_list)