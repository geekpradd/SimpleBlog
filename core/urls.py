from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createPost, name='createPost'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('view/<int:blog_id>', views.view, name='view'),
    path('register/', views.register, name='register')
]