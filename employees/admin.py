from django.contrib import admin

# Register your models here.
from .models import employees

class employeesAdmin(admin.ModelAdmin):
    list_display = ('employees_id','name','position','avata','file_image')
    search_fields = ['name']
    list_filter = ('employees_id','name','position','avata','file_image')

admin.site.register(employees, employeesAdmin)