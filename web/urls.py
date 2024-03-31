from django.urls import path
from web.views import scrap, search, estimate

app_name = 'web'

urlpatterns = [
    path('', scrap, name='scrap'),
    path('search/', search, name='search'),
    path('estimate/', estimate, name='estimate'),
]
