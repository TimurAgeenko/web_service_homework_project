from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    phone = forms.CharField(max_length=20, label='Телефон')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))
