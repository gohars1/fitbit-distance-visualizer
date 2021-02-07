from django.shortcuts import render
from django.http import HttpResponse
from fitbit.api import Fitbit
from urllib.parse import urlparse
import config
import threading
import webbrowser
import requests



CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
redirect_uri='http://127.0.0.1:8000/'
fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, redirect_uri, timeout=10)

# Create your views here.
def index(request):
    url, _ = fitbit.client.authorize_token_url()
    print(url)
    threading.Timer(1, webbrowser.open, args=(url,)).start()

    return HttpResponse("you made it" + url)

def test_endpoint(request, code, state):
    
    # fitbit.access_token = code
    access = fitbit.client.fetch_access_token(code)
    print(request.content_type)
  #  print(fitbit.activities())
    # bp = fitbit.bp()
    return HttpResponse("hello")