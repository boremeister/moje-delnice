from django.db import models
from django.conf import settings
import datetime

# stocks
class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    # define table name
    class Meta:
      db_table = "stocks"

    # show field in admin site
    def __str__(self):
        return self.code

# currencies
class Currency(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    # define table name
    class Meta:
      db_table = "currencies"

    # show field in admin site
    def __str__(self):
        return self.code

# exchange rates
class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    # define table name
    class Meta:
      db_table = "exchange_rates"

    # show field in admin site
    def __str__(self):
        return (self.currency.code + " - " + self.date.strftime('%Y-%m-%d'))

# dividends
class Dividende(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    dividende_value = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)    

    # define table name
    class Meta:
      db_table = "dividendes"

    # show field in admin site
    def __str__(self):
        return (self.stock + " - " + self.date.strftime('%Y-%m-%d'))

# stock prices
class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    # define table name
    class Meta:
      db_table = "stock_prices"

    # show field in admin site
    def __str__(self):
        return (self.stock + " - " + self.date.strftime('%Y-%m-%d'))

# tags
class Tag(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)
    
    # define table name
    class Meta:
      db_table = "tags"

    # show field in admin site
    def __str__(self):
        return self.name

# transactions
class Transaction(models.Model):
    BUY = 0
    SELL = 1
    TRANSACTION_TYPE = (
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    )
    transaction_type = models.IntegerField(default = 0, choices = TRANSACTION_TYPE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    provision = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    # define table name
    class Meta:
      db_table = "transactions"

      # show field in admin site
    def __str__(self):
        return (self.transaction_type + " - " + self.stock.code + " - " + self.date.strftime('%Y-%m-%d'))