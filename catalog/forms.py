from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Category, Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    phone = forms.CharField(max_length=20, label='Телефон')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию из списка",
        label="Категория продукта",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    spam = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'image', 'description')
        labels = {
            'name': 'Название товара',
            'price': 'Цена товара',
            'image': 'Выберете фото',
            'description': 'Описание',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(spam_word in word.lower() for spam_word in self.spam for word in name.split()):
            raise ValidationError('Имя не должно содержать спама.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(spam_word in word.lower() for spam_word in self.spam for word in description.split()):
            raise ValidationError('Описание не должно содержать спама.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена товара должна быть положительным числом.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        limit = 5 * 1024 * 1024
        if image.size > limit:
            raise ValidationError('Максимальный размер файла — 5 МБ.')
        return image
