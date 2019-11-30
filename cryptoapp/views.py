from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ('Welcome '+ username))
            return redirect('home')
        else:
            messages.success(request,('Incorrect Username/Password'))
            return redirect('login')
    return render(request,'login.html',{'title':'Login'})

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    messages.success(request,('Logout Successfully'))
    return render(request,'login.html',{'title':'Login'})

@login_required(login_url='/login/')
def home(request):
    import requests
    import json
    
    api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,XDA,USDT,MIOTA,TRX&tsyms=USD')
    price_api = json.loads(api_request.content)

    
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api': api, 'price': price_api})

@login_required(login_url='/login/')
def prices(request):
    if request.method == 'POST':      
        qoute = request.POST['qoute'].upper()
        qoute = qoute.replace(' ','')
        import requests
        import json
        
        api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+qoute+'&tsyms=USD')
        price_api = json.loads(api_request.content)
        return render(request, 'prices.html',{'qoute': qoute, 'crypto': price_api})
    return render(request, 'prices.html',{})