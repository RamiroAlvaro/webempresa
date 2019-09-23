from django.contrib import admin
from webempresa.services.models import Service


class ServiceModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceModelAdmin)
