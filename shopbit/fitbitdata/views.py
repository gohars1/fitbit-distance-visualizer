from django.shortcuts import redirect, render
from django.http import HttpResponse
from fitbit.api import Fitbit
from urllib.parse import urlparse
from .models import User, distance_hash
import config
import threading
import webbrowser
import requests
import json

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
redirect_uri='http://127.0.0.1:8000/'
fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, redirect_uri, timeout=10)

# Create your views here.
def index(request):
    url, _ = fitbit.client.authorize_token_url()#prompt="login")

    threading.Timer(1, webbrowser.open, args=(url,)).start()
    
    return HttpResponse("")

def test_endpoint(request):
    
    code = request.GET.get('code')
    access_token = fitbit.client.fetch_access_token(code)["access_token"]
    print(access_token)
    user_profile = fitbit.user_profile_get()
    encoded_id = user_profile['user']['encodedId']
    #new_user = User.objects.get_or_create(user_id=encoded_id, username=user_profile['user']['fullName'])
    #new_user.save()
    headers = {
            'Authorization': 'Bearer %s' % access_token
        }

    api_request = "https://api.fitbit.com/1/user/-/activities.json"
    life_time_stats = requests.get(api_request, headers=headers)
    print(json.dumps(life_time_stats.json()))
    # print(api_request)
    
    print(life_time_stats)
   # print(new_user.user_id, new_user.username)
    return HttpResponse("hello" + str(life_time_stats))