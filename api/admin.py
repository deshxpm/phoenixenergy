from django.contrib import admin
from .models import *
from import_export.admin import *

class EnergyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('time_series','voltage', 'current')

admin.site.register(Energy, EnergyAdmin)
