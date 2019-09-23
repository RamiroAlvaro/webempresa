from django.contrib import admin
from webempresa.blog.models import Category, Post


class CategoryModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías'


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
