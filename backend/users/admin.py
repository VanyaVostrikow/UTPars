from django.contrib import admin
from .models import Users

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'username', 'lastname', 'firstname')
    list_display_links = ('id', 'chat_id', 'username', 'lastname', 'firstname')
    list_filter = ('id', 'chat_id', 'username', 'lastname', 'firstname')
    fields = ['chat_id',('firstname', 'lastname'), ('username','email'),'country_id','language_id','want_recomend','rating']
    readonly_fields = ['date_create','date_change']
    search_fields = ('id', 'chat_id', 'username', 'lastname', 'firstname')
