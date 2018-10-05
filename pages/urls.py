from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    url('auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login, name='login'),

    path('stockprices/', views.stockprices, name='stockprices'),
    path('exchangerates/', views.exchangerates, name='exchangerates'),
    path('transactions/', views.transactions, name='transactions'),
    
    path('stocks/', views.stocks, name='stocks'),
    path('stocks/add', views.add_stock, name='add_stock'),
    path('stocks/edit/<int:id>', views.edit_stock, name='edit_stock'),
    path('stocks/delete/<int:id>', views.delete_stock, name='delete_stock'),

    path('currencies/', views.currencies, name='currencies'),
    path('currencies/add', views.add_currency, name='add_currency'),
    path('currencies/edit/<int:id>', views.edit_currency, name='edit_currency'),
    path('currencies/delete/<int:id>', views.delete_currency, name='delete_currency'),

    path('tags/', views.tags, name='tags'),
    path('tags/add', views.add_tag, name='add_tag'),
    path('tags/edit/<int:id>', views.edit_tag, name='edit_tag'),
    path('tags/delete/<int:id>', views.delete_tag, name='delete_tag'),
    
    path('users/', views.users, name='users'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]