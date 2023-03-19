from django.db import models
from django.contrib.auth.models import User


class DeviceTypes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    added_date = models.DateTimeField('added date')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_name = models.CharField(max_length=200)
    device_type = models.ForeignKey(DeviceTypes, on_delete=models.CASCADE)
    device_displayed_name = models.CharField(max_length=200, null=True, blank=True)
    device_description = models.CharField(max_length=400, null=True, blank=True)
    device_serial_number = models.CharField(max_length=100, null=True, blank=True)
    device_add_date = models.DateTimeField('Added')
    device_bought_date = models.DateTimeField('Bought')
    WARRANTY_CHOICE = (
        ('Active', 'Warranty still active'),
        ('Inactive', 'Warranty not activated'),
        ('Finished', 'Warranty finished')
    )
    device_warranty = models.CharField(max_length=10, choices=WARRANTY_CHOICE)
    user_connected = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_name

# Create your models here.
