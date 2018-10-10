from django.shortcuts import render, get_object_or_404
from . models import Currency, Stock, Tag, StockPrice, ExchangeRate, Dividende
from django.http import HttpResponse
from . forms import StockForm, CurrencyForm, TagForm, StockPriceForm, ExchangeRateForm, DividendForm
from django.shortcuts import redirect
import datetime

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "registration/login.html", {})

# stock prices
def stockprices(request):

    all_stockprices = StockPrice.objects.all()
    context = {
        'stockprices_list': all_stockprices
    }

    return render(request, "stockprices/stockprices.html", context)

def add_stockprice(request):

    if request.method == "POST":
        form = StockPriceForm(request.POST)
        if form.is_valid():
            stockprice = form.save(commit=False)
            stockprice.created_by = request.user
            stockprice.save()
            return redirect('stockprices')
    else:
        # preset date field to current date
        now = datetime.datetime.now()
        form = StockPriceForm(initial={'date':now.strftime("%Y-%m-%d")})
    
    return render(request, "stockprices/add_stockprice.html", {'form': form})

def edit_stockprice(request, id = None):

    stockprice = get_object_or_404(StockPrice, id = id)

    if request.method == "POST":
        form = StockPriceForm(request.POST, instance = stockprice)
        if form.is_valid():
            stockprice = form.save(commit=False)
            #stockprice.created_by = request.user
            stockprice.save()
            return redirect('stockprices')
    else:
        form = StockPriceForm(instance = stockprice)
    
    return render(request, "stockprices/edit_stockprice.html", {'form': form})

def delete_stockprice(request, id = None):

    stockprice = get_object_or_404(StockPrice, id = id)

    if request.method == "POST":
        stockprice.delete()
        return redirect('stockprices')
    else:   
        return render(request, "stockprices/delete_stockprice.html", {'stockprice': stockprice})

# dividends
def dividends(request):

    all_dividends = Dividende.objects.all()
    context = {
        'dividends_list': all_dividends
    }

    return render(request, "dividends/dividends.html", context)

def add_dividend(request):

    if request.method == "POST":
        form = DividendForm(request.POST)
        if form.is_valid():
            dividend = form.save(commit=False)
            dividend.created_by = request.user
            dividend.save()
            return redirect('dividends')
    else:
        # preset date field to current date
        now = datetime.datetime.now()
        form = DividendForm(initial={'date':now.strftime("%Y-%m-%d")})
    
    return render(request, "dividends/add_dividend.html", {'form': form})

def edit_dividend(request, id = None):

    dividend = get_object_or_404(Dividende, id = id)

    if request.method == "POST":
        form = DividendForm(request.POST, instance = dividend)
        if form.is_valid():
            dividend = form.save(commit=False)
            #stockprice.created_by = request.user
            dividend.save()
            return redirect('dividends')
    else:
        form = DividendForm(instance = dividend)
    
    return render(request, "dividends/edit_dividend.html", {'form': form})

def delete_dividend(request, id = None):

    dividend = get_object_or_404(Dividende, id = id)

    if request.method == "POST":
        dividend.delete()
        return redirect('dividends')
    else:   
        return render(request, "dividends/delete_dividend.html", {'dividend': dividend})

# exchange rates
def exchangerates(request):

    all_exchangerates = ExchangeRate.objects.all()
    context = {
        'exchangerates_list': all_exchangerates
    }

    return render(request, "exchangerates/exchangerates.html", context)

def add_exchangerate(request):

    if request.method == "POST":
        form = ExchangeRateForm(request.POST)
        if form.is_valid():
            exchangerate = form.save(commit=False)
            exchangerate.created_by = request.user
            exchangerate.save()
            return redirect('exchangerates')
    else:
        # preset date field to current date
        now = datetime.datetime.now()
        form = ExchangeRateForm(initial={'date':now.strftime("%Y-%m-%d")})
    
    return render(request, "exchangerates/add_exchangerate.html", {'form': form})

def edit_exchangerate(request, id = None):

    exchangerate = get_object_or_404(ExchangeRate, id = id)

    if request.method == "POST":
        form = ExchangeRateForm(request.POST, instance = exchangerate)
        if form.is_valid():
            exchangerate = form.save(commit=False)
            exchangerate.save()
            return redirect('exchangerates')
    else:
        form = ExchangeRateForm(instance = exchangerate)
    
    return render(request, "exchangerates/edit_exchangerate.html", {'form': form})

def delete_exchangerate(request, id = None):

    exchangerate = get_object_or_404(ExchangeRate, id = id)

    if request.method == "POST":
        exchangerate.delete()
        return redirect('exchangerates')
    else:   
        return render(request, "exchangerates/delete_exchangerate.html", {'exchangerate': exchangerate})

# transactions
def transactions(request):
    return render(request, "transactions.html", {})

# stocks
def stocks(request):
    
    all_stocks = Stock.objects.all()
    context = {
        'stocks_list': all_stocks
    }

    return render(request, "stocks/stocks.html", context)

def add_stock(request):

    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_by = request.user
            stock.save()
            return redirect('stocks')
    else:
        form = StockForm()
    
    return render(request, "stocks/add_stock.html", {'form': form})

def edit_stock(request, id = None):

    stock = get_object_or_404(Stock, id = id)

    if request.method == "POST":
        form = StockForm(request.POST, instance = stock)
        if form.is_valid():
            stock = form.save(commit=False)
            #stock.created_by = request.user
            stock.save()
            return redirect('stocks')
    else:
        form = StockForm(instance = stock)
    
    return render(request, "stocks/edit_stock.html", {'form': form})

def delete_stock(request, id = None):

    stock = get_object_or_404(Stock, id = id)

    if request.method == "POST":
        stock.delete()
        return redirect('stocks')
    else:   
        return render(request, "stocks/delete_stock.html", {'stock': stock})

# currencies
def currencies(request):

    all_currencies = Currency.objects.all()
    context = {
        'currencies_list': all_currencies
    }

    return render(request, "currencies/currencies.html", context)

def add_currency(request):

    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.created_by = request.user
            currency.save()
            return redirect('currencies')
    else:
        form = CurrencyForm()
    
    return render(request, "currencies/add_currency.html", {'form': form})

def edit_currency(request, id = None):

    currency = get_object_or_404(Currency, id = id)

    if request.method == "POST":
        form = CurrencyForm(request.POST, instance = currency)
        if form.is_valid():
            currency = form.save(commit=False)
            #currency.created_by = request.user
            currency.save()
            return redirect('currencies')
    else:
        form = CurrencyForm(instance = currency)
    
    return render(request, "currencies/edit_currency.html", {'form': form})

def delete_currency(request, id = None):

    currency = get_object_or_404(Currency, id = id)

    if request.method == "POST":
        currency.delete()
        return redirect('currencies')
    else:
        return render(request, "currencies/delete_currency.html", {'currency': currency})

# tags
def tags(request):
    
    all_tags = Tag.objects.all()
    context = {
        'tags_list': all_tags
    }

    return render(request, "tags/tags.html", context)

def add_tag(request):

    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.save()
            return redirect('tags')
    else:
        form = TagForm()
    
    return render(request, "tags/add_tag.html", {'form': form})

def edit_tag(request, id = None):

    tag = get_object_or_404(Tag, id = id)

    if request.method == "POST":
        form = TagForm(request.POST, instance = tag)
        if form.is_valid():
            tag = form.save(commit=False)
            #tag.created_by = request.user
            tag.save()
            return redirect('tags')
    else:
        form = TagForm(instance = tag)
    
    return render(request, "tags/edit_tag.html", {'form': form})

def delete_tag(request, id = None):

    tag = get_object_or_404(Tag, id = id)

    if request.method == "POST":
        tag.delete()
        return redirect('tags')
    else:
        return render(request, "tags/delete_tag.html", {'tag': tag})

def users(request):
    return render(request, "users.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})