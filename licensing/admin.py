from django.contrib import admin

# Register your models here.
from .models import Application, Lumber, Species, Profile, CITESList

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('importer_name', 'type', 'goods', 'importer_address', 'importer_city', 'importer_state', 'importer_phone', 'importer_email', 'exporter_name', 'exporter_address', 'exporter_city', 'exporter_state', 'mode_of_transport', 'port_of_entry', 'port_of_exit', 'treatment', 'date_received', 'date_approved', 'date_expires', 'packaging_list_approved', 'approval')

    search_fields = ('importer_name', 'type', 'goods', 'importer_address', 'importer_city', 'importer_state', 'importer_phone', 'importer_email', 'exporter_name', 'exporter_address', 'exporter_city', 'exporter_state', 'mode_of_transport', 'port_of_entry', 'port_of_exit', 'treatment', 'date_received', 'date_approved', 'date_expires', 'packaging_list_approved', 'approval')

class CITESListAdmin(admin.ModelAdmin):
    list_display = ('CITES_id', 'species', 'sub_species', 'scientific_name', 'rank', 'listing', 'common_name')

    search_fields = ('species', 'scientific_name', 'common_name')

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Lumber)
admin.site.register(Species)
admin.site.register(Profile)
admin.site.register(CITESList, CITESListAdmin)