from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from web.forms import house
from bs4 import BeautifulSoup
import re
import requests


# Create your views here.
def scrap(request):
    if request.method == 'POST':
        for i in range(200):
            base_url = f'https://kilid.com/buy-apartment/tehran?page={i}'
            response = requests.get(base_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                tags = soup.find_all('div',
                                     class_='flex flex-col flex-1 flex-grow h-48 min-h-[124px] justify-between pb-4')
                for tag in tags:
                    address = tag.find('p', class_='inline-flex text-grey-500').text.strip()
                    p = tag.find('span', class_='text-lg font-bold')
                    if p:
                        p = p.text.strip()
                    else:
                        p = "0"
                    price = re.search(r'\d+', p).group()
                    inner = tag.select('div.-m-2>span.text-grey-700')
                    metr = [0]
                    rooms = [0]
                    parking = [0]
                    for inn in inner:
                        s = inn.text
                        if re.search(r'متر', s):
                            metr.insert(0, re.search(r'\d+', s).group())
                        if re.search(r'خواب', s):
                            rooms.insert(0, re.search(r'\d+', s).group())
                        if re.search(r'پارکینگ', s):
                            parking.insert(0, re.search(r'\d+', s).group())

                    # اضافه کردن اطلاعات به رکورد مدل و ذخیره در پایگاه داده
                    if not house.objects.filter(location=address, metr=metr[0], parking=parking[0], rooms=rooms[0],
                                                price=price).exists():
                        h = house(location=address, metr=metr[0], parking=parking[0], rooms=rooms[0], price=price)
                        h.save()
        messages.success(request, 'ِData Scraped Successfully')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'scrap.html')


def search(request):
    if request.method == 'POST':

        location = request.POST.get('location')
        price = request.POST.get('price')
        rooms = request.POST.get('rooms')
        parking = request.POST.get('parking')
        metr = request.POST.get('metr')
        print(location, rooms, parking, metr, price)

        # بررسی اینکه آیا هرکدام از فیلدها خالی نیست
        if location or price or rooms or parking or metr:
            filter_args = {}
            if location:
                filter_args['location'] = location
            if price:
                filter_args['price'] = price
            if rooms:
                filter_args['rooms'] = rooms
            if parking:
                filter_args['parking'] = parking
            if metr:
                filter_args['metr'] = metr

        # انجام مقایسه با اطلاعات موجود در پایگاه داده با استفاده از فیلتر
            matched_data = house.objects.filter(**filter_args)

        # ارسال نتایج به قالب
            return render(request, 'search.html', {'matched_data': matched_data})
        else:
            # اگر هیچ فیلتری مشخص نشده باشد، پیغامی نمایش داده می‌شود
            return HttpResponse("Please specify at least one filter parameter.")
    else:
        return render(request, 'search.html')


def estimate(request):
    return render(request, 'estimate.html')
