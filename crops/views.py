from django.shortcuts import render,redirect
import requests
from .models import Data, savedata



def crops(request):
    llat=""
    llon=""
    temp=humidity=latitude=longitude=city=description=wind_speed=""
    obj= Data.objects.all()
    
    if request.method=='POST':
        lati = request.POST.dict()
        llat=lati.get("latitude")
        llon=lati.get("longitude")
        latitude = llat
        longitude = llon

        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=be3f016be8f78ecaa9522846c2fe4daf&units=metric'.format(latitude, longitude)

        res = requests.get(url)

        data = res.json()

        temp = data['main']['temp']
        humidity= data['main']['humidity']
        wind_speed = data['wind']['speed']

        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        city= data['name']
        description = data['weather'][-1]['description']
        print(city, temp)
        
    
    else:
        llat='1'
        llon='1'
         
        mapbox_access_token='pk.eyJ1Ijoicm9taXRzaW5naDE5OTkiLCJhIjoiY2tiNTR1aDM3MTFqbTJ3czc5dnVxZ3Q1dCJ9.6JV6YA9gjRfNaAqdiSScQQ'
        
        
    return render(request, 'base.html',
    {'mapbox_access_token':mapbox_access_token,'temp':temp,
        'obj':obj,
        'humidity':humidity,
        'wind':wind_speed,
        'city':city,
        'description':description})


def feature1(request):
    return render(request, 'Response1.html')

def feature2(request):
    return render(request, 'Response2.html')
def data(request):
    if request.is_ajax():
        if request.method=='POST':
            lati = request.POST.dict()
            llat=lati.get("latitude")
            llon=lati.get("longitude")
            latitude = llat
            longitude = llon

            url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=be3f016be8f78ecaa9522846c2fe4daf&units=metric'.format(latitude, longitude)

            res = requests.get(url)

            data = res.json()

            temp = data['main']['temp']
            humidity= data['main']['humidity']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']
            city= data['name']
            description = data['weather'][-1]['description']
            print(city, temp, longitude)
            saved = savedata.objects.create(city=city,temp=temp,wind=wind_speed,desc=description,lat=latitude,lon=longitude,humidity=humidity)
            saved.save()

            
            return render(request, 'newbase.html',{'city':city})    

    else:
        return render(request, 'base.html')

def show(request):
    obj= savedata.objects.all()
    obj=list(obj)
    obj.reverse()
    obj=obj[0]
    data={}
    
    if (float(obj.temp)<26 ):
        data['crop']='wheat, Onion'
    elif (float(obj.temp)<27 ):
        data['crop']='Maize , Pulses, Sugarcane'
    elif (float(obj.temp)<32 ):
        data['crop']='Rice, Cotton'
    elif (float(obj.temp)<38 ):
        data['crop']='Peanut/Groundnut'
    if (float(obj.wind)<3):
        data['wind']='light wind'
    elif (float(obj.wind)>3 and int(obj.wind)<10):
        data.append('Gentle breeze')
    elif (float(obj.wind)>10 and int(obj.wind)<16):
        data.append("Fresh breeze")
    elif (float(obj.wind)>16 and int(obj.wind)<28):
        data.append("strong breeze")
    elif(float(obj.wind)>38):
        data.append("Gale")
    
    print(obj)
    return render(request, 'newbase.html',{'obj':obj,'data':data})
