from django.contrib import admin
from .models import product

class productadmin(admin.ModelAdmin):
    list_display = ('p_name','p_choices','p_quantity')
    list_filter = ('p_name','p_choices')
    search_fields = ('p_name','p_choices','p_quantity')

admin.site.register(product,productadmin)