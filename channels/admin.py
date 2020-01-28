from django.contrib import admin
from .models import Channels


class ChannelsAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description')


# Register your models here.
admin.site.register(Channels, ChannelsAdmin)  # add this
