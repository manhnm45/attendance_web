from django.shortcuts import render, redirect
from .models import employees
from .form import employeeform
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import employeeSerializer, attendanceSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import mimetypes
import os
from datetime import timedelta
from .models import attendance
import datetime
from .filters import OrderFilter
import json
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def get_staffinfor(request):
    employees_list = employees.objects.filter().order_by('employees_id')
    return render(request, 'staff_infor.html', {'employees_list': employees_list})

def add_staff(request):
    return render(request,'add_staff.html')

def get_error(request):
    return render(request, 'error.html')
def save_staff_db(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        avata = request.FILES['avata']
        file_image = request.FILES['file_image']
        # print("avata",avata)
        # print("file_image",file_image)
        employee = employees.objects.create(name = name, position = position, avata= avata, file_image= file_image)
        employee.save()
        return redirect('liststaff')
    else:
        return render(request, 'error.html')

def delete(request, id):
    employee = employees.objects.get(employees_id= id)
    employee.delete()
    return redirect("liststaff")  

def delete_attendance(request, id):
    attenc = attendance.objects.get(id= id)
    attenc.delete()
    return redirect("attendance_holder")

def attendance_holder(request):
    attendance_list = attendance.objects.filter().order_by('date')
    myfilters = OrderFilter(request.GET, queryset= attendance_list)
    attendance_list = myfilters.qs
    qs_json = json.dumps(list(attendance.objects.values()))
    return render(request,"attendance.html", {'attendance_list': attendance_list , 'myfilters' : myfilters, 'qs_json' :qs_json})



def edit(request, id):
    employee = employees.objects.get(employees_id= id)
    form = employeeform(request.POST,instance= employee)
    if form.is_valid():
        form.save()
        return redirect("liststaff")
    return render(request,'edit.html',{'employee':employee})

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def ShowAll(request):
    if request.method == "GET":
        employee = employees.objects.all()
        serializer = employeeSerializer(employee, many = True)
        return Response(serializer.data)
    if request.method =="POST":
        
        employee = employees.objects.create(
            name = request.data['name'],
            position = request.data['position'],
            avata = request.data['avata'],
            file_image = request.data['file_image'],
        )
        serializer = employeeSerializer(employee, many = False)
        return Response(serializer.data)
@api_view(['GET',"PUT", "DELETE"])
def apidetail(request,id):
    employee = employees.objects.get(employees_id= id)
    if request.method == "GET":
        serializer = employeeSerializer(employee, many = False)
        return Response(serializer.data)
    if request.method == "PUT":
        employee.name = request.data['name']
        employee.position = request.data['position']
        employee.avata = request.data['avata']
        employee.file_image = request.data['file_image']
        
        employee.save()
        serializer = employeeSerializer(employee, many = False)
        return Response(serializer.data)
    if request.method == "DELETE":
        employee.delete()
        return Response("delete success")

@api_view(["GET","POST"])    
def serve_img(request,image_name):
    try:
        # Open the image file in binary mode
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_dir = os.path.join(base_dir,'home/media/Image')
        print("media_dir",media_dir)
        image_path = os.path.join(media_dir,image_name)
        print("image_path",image_path)
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Use mimetypes module for reliable MIME type detection
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = 'application/octet-stream'  # Default for unknown types

        # Create the response and set the content type
        response = HttpResponse(image_data, content_type=mime_type)

        # Optionally set Content-Disposition to display or download
        # Customize as needed (e.g., use the original filename)
        # response['Content-Disposition'] = 'inline; filename="myimage.jpg"'
        print("response",response)
        return response

    except FileNotFoundError:
        # Handle file not found error (e.g., return a 404 response)
        return HttpResponse(status=404)

    except Exception as e:
        # Handle other errors (e.g., log the error and return a 500 response)
        print(f"Error serving image: {e}")
        return HttpResponse(status=500)
    
request_list = []  
attendance_in = []
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def attendance_api(request):
    
    print("type time",type(request.data['time']))
    iso_timestamp = request.data['time']
    
    dt = datetime.datetime.fromisoformat(iso_timestamp)
    time_str = dt.strftime("%H:%M:%S")
    dates = f"{dt.year}-{dt.month}-{dt.day}"
    Employee = employees.objects.get(employees_id =request.data['id'])
    if len(request_list) ==0:
        #request_list.append(request)
        time_ins = time_str
        time_outs = "working"
        print("lenreques=0")
        attendances = attendance.objects.create(
                    employee = Employee,
                    date = dates,
                    time_in = time_ins,
                    time_out = time_outs,
                    location_check = request.data['location check']
                )
        serializer = attendanceSerializer(attendances, many = False)
        request_list.append(request)
        #request_list.clear()
    else:
        for requests in request_list:
            check_in = False
            if requests.data['id'] == request.data['id']:
                print("checked")
                check_in = True
                time_outs = time_str
                attendances = attendance.objects.get(employee = Employee, date = dates)
                print("attendance_timeout",attendances.time_out)
                attendances.time_out = time_outs
                print("attendance_timeout2",attendances.time_out)
                attendances.save()
                serializer = attendanceSerializer(attendances, many = False)
                request_list.remove(requests)
                break
        if check_in == False:
            print("checkin false")
            request_list.append(request)
            time_ins = time_str
            time_outs = "working"
            #request_list.clear()
            attendances = attendance.objects.create(
                employee = Employee,
                date = dates,
                time_in = time_ins,
                time_out = time_outs,
                location_check = request.data['location check']
            )
            serializer = attendanceSerializer(attendances, many = False)
    return Response(serializer.data)



def search_attendance(request):
    filter_value = request.POST['filter']
    print("filter_value",filter_value)
    filtered_data = attendance.objects.filter(
    Q(date__icontains=filter_value) | Q(location_check__icontains=filter_value) | Q(employee__name__icontains=filter_value))
    data_list=[{
        'id':obs.id ,'id_staff': obs.id_staff, 'name': obs.name,'date': obs.date, 'time_in':obs.time_in, 'time_out': obs.time_out, 'location_check': obs.location_check 
    } for obs in filtered_data
    ]
    #print(data_list)
    return JsonResponse({'data': data_list})

def visual_employee(request):
    return render(request,'visual_employee.html')