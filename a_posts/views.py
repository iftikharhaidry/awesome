from django.shortcuts import render
from .models import *
# Create your views here.
def home_view(request):
    print(request.META)
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'a_posts/home.html', context)