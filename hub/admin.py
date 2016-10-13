from django.contrib import admin

from .models import Art, Category


class ArtAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Art, ArtAdmin)
admin.site.register(Category, CategoryAdmin)

