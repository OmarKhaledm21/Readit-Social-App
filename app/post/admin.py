from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','slug','community')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
