from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on', 'updated_on')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
# admin.site.register(Post, PostAdmin)
