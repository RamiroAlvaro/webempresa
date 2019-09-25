from django.contrib import admin
from webempresa.social.models import Link


class LinkModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkModelAdmin)
