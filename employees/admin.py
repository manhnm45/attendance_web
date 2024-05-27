from django.contrib import admin

# Register your models here.
from .models import employees
from .models import attendance
class employeesAdmin(admin.ModelAdmin):
    list_display = ('employees_id','name','position','avata','file_image')
    search_fields = ['name']
    list_filter = ('employees_id','name','position','avata','file_image')

admin.site.register(employees, employeesAdmin)

class attendancesAdmin(admin.ModelAdmin):
    list_display = ('employee','date','time_in','time_out','location_check')
    search_fields = ['date']
    list_filter = ('employee','date','time_in','time_out','location_check')

admin.site.register(attendance, attendancesAdmin)
