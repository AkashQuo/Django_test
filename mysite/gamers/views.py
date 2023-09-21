from django.shortcuts import render
from .models import GAMER_USER

def post_list(request):
    posts = GAMER_USER.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})