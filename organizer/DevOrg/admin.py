from django.contrib import admin

from .models import Device, DeviceTypes

admin.site.register(Device)
admin.site.register(DeviceTypes)

# Register your models here.
