from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [

    # default
    path('', views.home, name='home'),
    url('auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login, name='login'),

    # stock prices
    path('stockprices/', views.stockprices, name='stockprices'),
    path('stockprices/add', views.add_stockprice, name='add_stockprice'),
    path('stockprices/edit/<int:id>', views.edit_stockprice, name='edit_stockprice'),
    path('stockprices/delete/<int:id>', views.delete_stockprice, name='delete_stockprice'),

    # exchange rates
    path('exchangerates/', views.exchangerates, name='exchangerates'),
    path('exchangerates/add', views.add_exchangerate, name='add_exchangerate'),
    path('exchangerates/edit/<int:id>', views.edit_exchangerate, name='edit_exchangerate'),
    path('exchangerates/delete/<int:id>', views.delete_exchangerate, name='delete_exchangerate'),

    # transactions
    path('transactions/', views.transactions, name='transactions'),
    
    # stocks
    path('stocks/', views.stocks, name='stocks'),
    path('stocks/add', views.add_stock, name='add_stock'),
    path('stocks/edit/<int:id>', views.edit_stock, name='edit_stock'),
    path('stocks/delete/<int:id>', views.delete_stock, name='delete_stock'),

    # currencies
    path('currencies/', views.currencies, name='currencies'),
    path('currencies/add', views.add_currency, name='add_currency'),
    path('currencies/edit/<int:id>', views.edit_currency, name='edit_currency'),
    path('currencies/delete/<int:id>', views.delete_currency, name='delete_currency'),

    # tags
    path('tags/', views.tags, name='tags'),
    path('tags/add', views.add_tag, name='add_tag'),
    path('tags/edit/<int:id>', views.edit_tag, name='edit_tag'),
    path('tags/delete/<int:id>', views.delete_tag, name='delete_tag'),
    
    # other
    path('users/', views.users, name='users'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]