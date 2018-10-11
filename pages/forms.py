from django import forms
from . models import Tag, Stock, Currency, StockPrice, ExchangeRate, Dividende, Transaction

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

class ExchangeRateForm(forms.ModelForm):

    class Meta:
        model = ExchangeRate
        fields = ('currency', 'rate', 'date')

class DividendForm(forms.ModelForm):

    class Meta:
        model = Dividende
        fields = ('stock', 'dividende_value', 'currency', 'date')

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('transaction_type', 'stock', 'quantity', 'price', 'provision', 'currency', 'date', 'tag')