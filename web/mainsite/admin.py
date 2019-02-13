from django.contrib import admin
from .models import Post
# Register your models here.
from .models import Essay
# admin.site.register(Post)


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Essay)
