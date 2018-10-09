from django.contrib import admin
from pages.models import Stock, Currency, Dividende, StockPrice, Tag, Transaction, ExchangeRate

# Register your models here.
admin.site.register(Stock)
admin.site.register(Currency)
admin.site.register(Dividende)
admin.site.register(StockPrice)
admin.site.register(Tag)
admin.site.register(Transaction)
admin.site.register(ExchangeRate)