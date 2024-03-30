from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'public_date', 'views_count')
    list_filter = ('public_date',)
    search_fields = ('title', 'content')