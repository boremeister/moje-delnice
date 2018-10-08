from django import forms
from . models import Tag, Stock, Currency, StockPrice

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('code', 'name',)

class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('code', 'name',)

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name', 'description',)

class StockPriceForm(forms.ModelForm):

    class Meta:
        model = StockPrice
        fields = ('stock', 'price', 'currency', 'date')
