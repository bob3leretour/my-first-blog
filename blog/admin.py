from django.contrib import admin
from .models import Post,Category,Main_category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Main_category)