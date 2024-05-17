from django.shortcuts import render, redirect
from .models import employees
from .form import employeeform
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import employeeSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import mimetypes
import os
from datetime import timedelta
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