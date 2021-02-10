from fitbitdata.models import User
from fitbit.api import Fitbit
import config

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
redirect_uri='http://127.0.0.1:8000/'

def create_fitbit_with_cookies(request):
    access_token = request.COOKIES.get('token')
    refresh_token = request.COOKIES.get('refresh')
    expires_at = request.COOKIES.get('expires_at')
    # refresh_cb = request.COOKIES.get('refresh_cb')
    fitbit = Fitbit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, timeout=10, access_token=access_token
    , refresh_token=refresh_token, expires_at=expires_at)
    return fitbit

def get_user_with_client(fitbit):
    user_profile = fitbit.user_profile_get()
    user_id = user_profile["user"]["encodedId"]
    user = User.objects.get(user_id=user_id)
    return user

