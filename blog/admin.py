from django.contrib import admin
from .models import Post, Comment, Profile, UserFollow, UserLikePost, Notification


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "author")
    list_display_links = ("id", "author")
    list_filter = ("created_at", "author")

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "receiver", "sender", "type")
    list_display_links = ("id", "receiver", "sender", "type")
    list_filter = ("created_at", "type", "sender")

class UserLikePostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "author")
    list_display_links = ("id", "created_at", "author")
    list_filter = ("created_at", "author")

class UserFollowAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "follower", "following")
    list_display_links = ("id", "follower", "following")
    list_filter = ("created_at", "following")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")
    list_filter = ("id", "user")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "author")
    list_display_links = ("id", "author")
    list_filter = ("created_at", "author")

admin.site.register(UserFollow, UserFollowAdmin)
admin.site.register(UserLikePost, UserLikePostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification, NotificationAdmin)
