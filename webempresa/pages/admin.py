from django.contrib import admin
from webempresa.pages.models import Page


class PageModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')


admin.site.register(Page, PageModelAdmin)
