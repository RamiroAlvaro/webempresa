from django.contrib import admin
from webempresa.pages.models import Page


class PageModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Page, PageModelAdmin)
