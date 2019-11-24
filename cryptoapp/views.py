from django.shortcuts import render
from django.template import loader
# Create your views here.
def home(request):
    import requests
    import json
    
    api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,XDA,USDT,MIOTA,TRX&tsyms=USD')
    price_api = json.loads(api_request.content)

    
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api': api, 'price': price_api})

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