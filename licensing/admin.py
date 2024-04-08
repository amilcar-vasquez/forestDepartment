from django.contrib import admin

# Register your models here.
from .models import Application, Lumber, Species, SpeciesType, Profile

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('importer_name', 'type', 'goods', 'importer_address', 'importer_city', 'importer_state', 'importer_phone', 'importer_email', 'exporter_name', 'exporter_address', 'exporter_city', 'exporter_state', 'mode_of_transport', 'port_of_entry', 'port_of_exit', 'treatment', 'date_received', 'date_approved', 'date_expires', 'packaging_list_approved', 'approval')

    search_fields = ('importer_name', 'type', 'goods', 'importer_address', 'importer_city', 'importer_state', 'importer_phone', 'importer_email', 'exporter_name', 'exporter_address', 'exporter_city', 'exporter_state', 'mode_of_transport', 'port_of_entry', 'port_of_exit', 'treatment', 'date_received', 'date_approved', 'date_expires', 'packaging_list_approved', 'approval')

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Lumber)
admin.site.register(Species)
admin.site.register(SpeciesType)
admin.site.register(Profile)