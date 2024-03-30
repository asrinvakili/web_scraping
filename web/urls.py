from django.urls import path
from web.views import scrapping

app_name = 'web'

urlpatterns = [
    path('', scrapping, name='index'),
]
