from django.contrib import admin
from .models import Room, Topic, Message, User

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')

class UserAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')

class TopicAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')

class MessageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')

admin.site.register(User, UserAdmin)
admin.site.register(Room, MessageAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)

