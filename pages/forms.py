from django import forms
from . models import Tag, Stock, Currency

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name', 'description',)

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('code', 'name',)

class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('code', 'name',)