from django.shortcuts import render
from .models import employees
# Create your views here.
def get_staffinfor(request):
    employees_list = employees.objects.filter().order_by('employees_id')
    return render(request, 'staff_infor.html', {'employees_list': employees_list})