from django.forms import ModelForm
from main.models import Item
from django import forms
from django.core.validators import MinValueValidator


class ItemForm(ModelForm):
    amount = forms.IntegerField(
        validators=[MinValueValidator(limit_value=1, message="Amount must be greater than 0.")]
    )
    class Meta:
        model = Item
        fields = ["album", "year", "amount", "artist"]