
# Create your views here.
from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    # countrycode=request.get['ccode'];
    # phonenumber=request.get['pn'];
    response = requests.get('http://apilayer.net/api/validate?access_key=81f511599e67f381ac1ff12743ca4753&number=9618467907&country_code=IN&format=1')
    data = response.json()
    return render(request, 'core/home.html', {
        'data':data
    })


def verify(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

