from django.contrib import admin

# Register your models here.
from .models import BlogEntry

admin.site.register(BlogEntry)