from django.contrib import admin
from .models import Appliance

@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ['appliances', 'power', 'hours', 'days']
    fields = ['appliances', 'power', 'hours', 'days']

# Register your models here.
