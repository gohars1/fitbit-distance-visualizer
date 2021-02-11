from django.http import HttpResponse
from django.template import loader
from fitbit.api import Fitbit
from urllib.parse import urlparse
from .models import User
from socialapp.models import Post
from .utils import *
import config
import threading
import webbrowser


CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
redirect_uri='http://127.0.0.1:8000/'

# Create your views here.
def fitbit_login(request):
    
    fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, redirect_uri, timeout=10)

    url, _ = fitbit.client.authorize_token_url(prompt="login")

    threading.Timer(1, webbrowser.open, args=(url,)).start()
    
    return HttpResponse("")


def main_page(request):
    access_token = request.COOKIES.get('token')
    template = loader.get_template('fitbitdata/main_page.html')

    if not access_token:
        fitbit = Fitbit(CLIENT_ID, CLIENT_SECRET, redirect_uri, timeout=10)
        code = request.GET.get('code')
        tokens = fitbit.client.fetch_access_token(code)
        access_token = tokens["access_token"]
        refresh_token = tokens["refresh_token"]
        expires_at = int(tokens["expires_at"])
        lifetime_activity = get_lifetime_activity(access_token)
        new_user = create_or_update_user(fitbit, access_token)
        user_posts = Post.objects.filter(user_id=new_user[0]) 
        context = { 'lifetime_distance' : lifetime_activity["lifetime"]["total"]["distance"], 
            'lifetime_floors' : lifetime_activity["lifetime"]["total"]["floors"],
            'user_posts' : user_posts  }
        response = HttpResponse(template.render(context, request))
        response.set_cookie(key='token' ,value=access_token)
        response.set_cookie(key='refresh', value=refresh_token)
        response.set_cookie(key='expires_at', value=expires_at)

        return response
    else:
        fitbit = create_fitbit_with_cookies(request)# fitbit.client.access_token = access_token
        lifetime_distance = get_lifetime_from_cookies(request)[0]
        lifetime_floors = get_lifetime_from_cookies(request)[1]
        new_user = create_or_update_user(fitbit, access_token)
        user_posts = Post.objects.filter(user_id=new_user[0]) 
        context = { 'lifetime_distance' : lifetime_distance, 'lifetime_floors' : lifetime_floors, 'user_posts' : user_posts }
        response = HttpResponse(template.render(context, request))
        return response

def view_badges(request):
    token = request.COOKIES.get('token')
    lifetime_data = get_lifetime_activity(token)
    lifetime_distance = lifetime_data["lifetime"]["total"]["distance"]
    lifetime_floors = lifetime_data["lifetime"]["total"]["floors"]
    distance_badges = get_distance_badges(lifetime_distance)
    floors_badges = get_floors_badges(lifetime_floors)
    print(distance_badges)
    template = loader.get_template('fitbitdata/view_badges.html')
    context = { 'distance_badges' : distance_badges, 'floors_badges': floors_badges }

    return HttpResponse(template.render(context, request))


#           login with bitbit -> main menu (maybus it has a feed) it also has a side navbar where you can access profile 
#           In the profile you can view your badges, and you can see in progress badges. If a badge is complete you can share
#           it to the feed.
#  
#           Possible Features: Daily Calorie burn leaderboard. 
#
#           when you log in you pull the data from gitbit. 