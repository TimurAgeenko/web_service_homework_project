from django import forms

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
