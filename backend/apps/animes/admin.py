from django.contrib import admin
from .models import Anime, Category, Favourite, Comment


admin.site.register(Anime)
admin.site.register(Category)
admin.site.register(Favourite)
admin.site.register(Comment)
