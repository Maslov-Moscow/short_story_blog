from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "confirmed", "code")
    empty_value_display = "-пусто-"


admin.site.register(Profile, ProfileAdmin)
