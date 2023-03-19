from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Device, DeviceTypes

from . import specific_data


class SingUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"


def device_view(request):
    device_table = Device.objects.order_by('id')
    context = {
        'device_table': device_table
    }
    return render(request, 'device_view.html', context)


def add_device_view(request):
    specific_fields = specific_data.SpecificFieldsToShow()
    types_table = DeviceTypes.objects.order_by('name')
    context = {
        'fields_name': specific_fields.return_devices_fields_names_to_show(),
        'date_field': specific_fields.return_date_field_names(),
        'type_option_field': specific_fields.return_type_option_field_name(),
        'warranty_option_field': specific_fields.return_warranty_option_field_name(),
        'device_type': types_table
    }
    return render(request, 'expand/add_device.html', context)


def add_device_submit(request):
    device = get_object_or_404(Device)

    # Create your views here.
