# from django.http import HttpResponse
# from django.shortcuts import render
# from fitbitdata.models import User
# from .utils import create_fitbit_with_cookies, get_distance_badges, get_floors_badges
# from django.template import loader

# # Create your views here.
# def view_badges(request):
#     fitbit = create_fitbit_with_cookies(request)
#     fitbit.
#     life_time_distance = user.life_time_km
#     life_time_floors = user.life_time_floors
#     distance_badges = get_distance_badges(life_time_distance)
#     floors_badges = get_floors_badges(life_time_floors)
#     template = loader.get_template('socialapp/view_badges.html')
#     context = { 'distance_badges' : distance_badges, 'floors_badges': floors_badges }

#     return HttpResponse(template.render(context, request))