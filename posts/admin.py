from django.contrib import admin
from .models import Post, Vote

admin.site.register(Post)
admin.site.register(Vote)

admin.site.site_header = 'Oslo Hi-Fi Center administration'
# Register your models here.
