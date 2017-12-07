from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Like, Follow, User
from artists.models import Artist
# Register your models here.


class LikeInline(admin.StackedInline):
    model = Like
    can_delete = False

class MyUserAdmin(admin.ModelAdmin):
    list_display = ("nickname", "ucity")
    search_fields = ('nickname',)
    inlines = (LikeInline, )

class FollowAdmin(admin.ModelAdmin):
    list_display = ("followee", "follower")

class LikeAdmin(admin.ModelAdmin):
    list_display = ("get_user", "get_artist")


admin.site.register(Follow, FollowAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(MyUser, MyUserAdmin)

