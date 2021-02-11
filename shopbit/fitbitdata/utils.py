from .models import distance_hash, floors_hash, User
from fitbit.api import Fitbit
import config
import datetime
import json
import requests

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
redirect_uri='http://127.0.0.1:8000/'


def get_lifetime_activity(token):
    request_url = "https://api.fitbit.com/1/user/-/activities.json"
    headers = {
            'Authorization': 'Bearer %s' % token
    }
    life_time_activity = json.loads(requests.get(request_url, headers=headers).text)
    
    return life_time_activity

def get_distance_badges(lifetime_km):
    distance_badges = []
    for distance in distance_hash:
        achieved = False
        if (distance <= lifetime_km):
            achieved = True
        distance_badges.append((achieved, distance_hash[distance]))
    return distance_badges

def get_floors_badges(lifetime_floors):
    floors_badges = []
    for floors in floors_hash:
        achieved = False
        if (floors <= lifetime_floors):
            achieved = True
        floors_badges.append((achieved, floors_hash[floors]))
    return floors_badges
    
def create_or_update_user(fitbit, access_token):
    user_profile = fitbit.user_profile_get()
    encoded_id = user_profile['user']['encodedId']
    life_time_stats = get_lifetime_activity(access_token)
    life_time_km = life_time_stats["lifetime"]["total"]["distance"]
    life_time_floors = life_time_stats["lifetime"]["total"]["floors"]
    new_user = User.objects.get_or_create(user_id=encoded_id, username=user_profile['user']['fullName'])
    return new_user

def create_fitbit_with_cookies(request):
    access_token = request.COOKIES.get('token')
    refresh_token = request.COOKIES.get('refresh')
    expires_at = request.COOKIES.get('expires_at')
    # refresh_cb = request.COOKIES.get('refresh_cb')
    fitbit = Fitbit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, timeout=10, access_token=access_token
    , refresh_token=refresh_token, expires_at=expires_at)
    return fitbit

def get_lifetime_from_cookies(request):
    token = request.COOKIES.get('token')
    lifetime_data = get_lifetime_activity(token)
    lifetime_distance = lifetime_data["lifetime"]["total"]["distance"]
    lifetime_floors = lifetime_data["lifetime"]["total"]["floors"]
    return (lifetime_distance, lifetime_floors)