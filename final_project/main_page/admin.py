from django.contrib import admin
from .models import Post, Like, Category, Tag, Comment, Images

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Images)