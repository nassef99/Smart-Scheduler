from django.contrib import admin
from scheduler.models import Event


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
