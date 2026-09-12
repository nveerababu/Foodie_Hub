from django.contrib import admin
from .models import MenuItem
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'price', 'image_path')
    list_filter = ('category',)
    search_fields = ('name',)
# Register your models here.
