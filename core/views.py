from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import datetime
from .models import BlogEntry

# Create your views here.

def home(request):
    posts = BlogEntry.objects.order_by('-pubDate')
    context = {"posts": posts}
    return render(request, "home.html", context)

@login_required
def createPost(request):
    if request.method == "GET":
        return render(request, "new.html")
    
    heading = request.POST["heading"]
    article = request.POST["content"]
    BlogEntry.objects.create(article=article, heading=heading, author=request.user, pubDate=datetime.datetime.now())

    return redirect(home)

@login_required
def profile(request):
    posts = request.user.blogentry_set.all()
    return render(request, "profile.html", {"posts":posts})

def register(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect(home)
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def edit(request, blog_id):
    post = BlogEntry.objects.get(id=blog_id)
    if post.author != request.user:
        return redirect(home)
    if request.method == "GET":
        return render(request, "edit.html", {"post": post})
    
    heading = request.POST["heading"]
    article = request.POST["content"]
    post.heading = heading
    post.article = article
    post.save()
    return redirect(profile)

def view(request, blog_id):
    post = BlogEntry.objects.get(id=blog_id)
    return render(request, "view.html", {"post":post})
