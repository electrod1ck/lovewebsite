from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountCreationForm(forms.Form):
    CURRENCY_CHOICES = [
        ('RUB', 'Российский рубль (RUB)'),
        ('EUR', 'Евро (EUR)'),
        ('USD', 'Доллар США (USD)'),
        ('BYN', 'Белорусский рубль (BYN)'),
        ('KZT', 'Казахстанский тенге (KZT)'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('current', 'Текущий'),
        ('credit', 'Кредитный'),
        ('deposit', 'Депозитный'),
        ('savings', 'Накопительный'),
        ('budget', 'Бюджетный'),
    ]

    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label='Валюта')
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, label='Тип счёта')

class CustomUserCreationForm(UserCreationForm):
    passport_combined = forms.CharField(max_length=11, label='Серия и номер паспорта')
    secretword = forms.CharField(max_length=150, label='Кодовое слово')

    class Meta:
        model = User
        fields = ('username', 'password', 'passport_combined', 'secretword')