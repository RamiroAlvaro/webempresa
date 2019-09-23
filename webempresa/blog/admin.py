from django.contrib import admin
from webempresa.blog.models import Category, Post


class CategoryModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
