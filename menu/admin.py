from django.contrib import admin

from menu.models import Menu, ItemMenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(ItemMenu)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    list_filter = ('menu',)
