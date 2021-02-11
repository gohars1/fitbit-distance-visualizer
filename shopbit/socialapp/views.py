from .utils import create_fitbit_with_cookies, get_user_with_client
from django.http import HttpResponse
# from django.shortcuts import render
from fitbitdata.models import User
from .models import Post
# from .utils import create_fitbit_with_cookies, get_distance_badges, get_floors_badges
from django.template import loader

# # Create your views here.
def share_badge(request):
    badgename = request.POST.get('badgename')
    fitbit = create_fitbit_with_cookies(request)
    user = get_user_with_client(fitbit)
    username = user.username
    text = "I earned the " + badgename + " badge!"
    post = Post(text=text, user_id=user, username=username)
    post.save()
    return HttpResponse("hello")

def delete_post(request):
    post_id = request.POST.get('post_id')
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponse("deleted")

def view_feed(request):
    posts = Post.objects.all()
    template = loader.get_template('socialapp/view_feed.html')
    context = { 'posts' : posts }
    return HttpResponse(template.render(context, request))

