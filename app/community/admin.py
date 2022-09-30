from django.contrib import admin
from .models import Community, UserCommunity
# Register your models here.

class UserCommunityAdmin(admin.ModelAdmin):
    list_display = ('user','community')


class CommunityAdmin(admin.ModelAdmin):
    list_display =('id','community_name','description')
    
admin.site.register(Community,CommunityAdmin)
admin.site.register(UserCommunity,UserCommunityAdmin)
