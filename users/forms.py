from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)

        if 'username' in self.fields:
            self.fields['username'].label = "Электронная почта"

        if 'password' in self.fields:
            self.fields['password'].label = "Пароль"

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'password1', 'password2')

        labels = {
            'email': 'Электронная почта',
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Номер телефона',
            'country': 'Страна',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.error_messages = {
            'password_mismatch': 'Пароли не совпадают. Попробуйте ещё раз.',
        }

        if 'password1' in self.fields:
            self.fields['password1'].label = "Пароль"

        if 'password2' in self.fields:
            self.fields['password2'].label = "Подтвердите пароль"

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ''

            if field.required:
                field.label = f"{field.label}*"


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'country')

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Номер телефона',
            'country': 'Страна',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})