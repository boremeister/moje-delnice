from django.shortcuts import render, get_object_or_404
from . models import Currency, Stock, Tag
from django.http import HttpResponse
from . forms import TagForm, StockForm, CurrencyForm
from django.shortcuts import redirect

from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

class TagDeleteView(PassRequestMixin, SuccessMessageMixin,generic.CreateView):
    template_name = 'delete_tag.html'
    form_class = TagForm
    success_message = 'Success: Tag was deleted.'
    success_url = reverse_lazy('tags')

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "registration/login.html", {})

def stockprices(request):
    return render(request, "stockprices.html", {})

def exchangerates(request):
    return render(request, "exchangerates.html", {})

def transactions(request):
    return render(request, "transactions.html", {})

# stocks
def stocks(request):
    
    all_stocks = Stock.objects.all()
    context = {
        'stocks_list': all_stocks
    }

    return render(request, "stocks.html", context)

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
    
    return render(request, "add_stock.html", {'form': form})

def edit_stock(request, id = None):

    stock = get_object_or_404(Stock, id = id)

    if request.method == "POST":
        form = StockForm(request.POST, instance = stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_by = request.user
            stock.save()
            return redirect('stocks')
    else:
        form = StockForm(instance = stock)
    
    return render(request, "edit_stock.html", {'form': form})

def delete_stock(request, id = None):

    stock = get_object_or_404(Stock, id = id)

    if request.method == "POST":
        stock.delete()
        return redirect('stocks')
    else:   
        return render(request, "delete_stock.html", {'stock': stock})

# currencies
def currencies(request):

    all_currencies = Currency.objects.all()
    context = {
        'currencies_list': all_currencies
    }

    return render(request, "currencies.html", context)

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
    
    return render(request, "add_currency.html", {'form': form})

def edit_currency(request, id = None):

    currency = get_object_or_404(Currency, id = id)

    if request.method == "POST":
        form = CurrencyForm(request.POST, instance = currency)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.created_by = request.user
            currency.save()
            return redirect('currencies')
    else:
        form = CurrencyForm(instance = currency)
    
    return render(request, "edit_currency.html", {'form': form})

def delete_currency(request, id = None):

    currency = get_object_or_404(Currency, id = id)

    if request.method == "POST":
        currency.delete()
        return redirect('currencies')
    else:
        return render(request, "delete_currency.html", {'currency': currency})

# tags
def tags(request):
    
    all_tags = Tag.objects.all()
    context = {
        'tags_list': all_tags
    }

    return render(request, "tags.html", context)

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
    
    return render(request, "add_tag.html", {'form': form})

def edit_tag(request, id = None):

    tag = get_object_or_404(Tag, id = id)

    if request.method == "POST":
        form = TagForm(request.POST, instance = tag)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.save()
            return redirect('tags')
    else:
        form = TagForm(instance = tag)
    
    return render(request, "edit_tag.html", {'form': form})

def delete_tag(request, id = None):

    tag = get_object_or_404(Tag, id = id)

    if request.method == "POST":
        tag.delete()
        return redirect('tags')
    else:
        return render(request, "delete_tag.html", {'tag': tag})

def users(request):
    return render(request, "users.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})