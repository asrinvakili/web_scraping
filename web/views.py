from django.shortcuts import render


# Create your views here.
def scrapping(request):
    return render(request, 'index.html')
