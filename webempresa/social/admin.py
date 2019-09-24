from django.contrib import admin
from webempresa.social.models import Link


class LinkModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Link, LinkModelAdmin)
