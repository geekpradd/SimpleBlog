from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, views as loginViews
from django.contrib.auth.models import User
from django.contrib import messages
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
    subheading = request.POST["subheading"]
    BlogEntry.objects.create(article=article, heading=heading, author=request.user,subheading=subheading, pubDate=datetime.datetime.now())

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
            messages.add_message(request, messages.INFO, "You have successfully signed up. Login into your account")
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def delete(request, blog_id):
    post = BlogEntry.objects.get(id=blog_id)
    if post.author == request.user:
        post.delete()
    
    return redirect(profile)


@login_required
def edit(request, blog_id):
    post = BlogEntry.objects.get(id=blog_id)
    if post.author != request.user:
        return redirect(home)
    if request.method == "GET":
        return render(request, "edit.html", {"post": post})
    
    heading = request.POST["heading"]
    article = request.POST["content"]
    subheading = request.POST["subheading"]
    post.heading = heading
    post.article = article
    post.subheading = subheading
    post.save()
    return redirect(profile)

def view(request, blog_id):
    post = BlogEntry.objects.get(id=blog_id)
    return render(request, "view.html", {"post":post})
