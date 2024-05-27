"""manage_staff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home
from employees import views as employee
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    #TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.get_home, name = 'home'),
    path('employee/', employee.get_staffinfor, name = 'employee'),
    path('doLogin', home.do_login, name = "doLogin"),
    path('home/', home.home_holder,name='home_holder'),
    path('logout_user',home.logout_user, name ='logout'),
    path('liststaff',home.check_list_staff,name='liststaff'),
    path('add_staff',employee.add_staff, name='add_staff'),
    path('savedb',employee.save_staff_db, name = 'savedb'),
    path('error',employee.get_error, name='error'),
    path('delete/<int:id>',employee.delete,name = 'delete'),
    path('edit/<int:id>',employee.edit,name = 'edit'),
    path('api-list/',employee.ShowAll, name = 'api-list'),
    path("api-detail/<int:id>",employee.apidetail, name = 'apidetail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('images/<str:image_name>/', employee.serve_img, name='serve_image'),
    path('attendance_holder/', employee.attendance_holder, name ='attendance_holder'),
    path('api-attendance',employee.attendance_api, name = 'api-attendance'),
    path('delete_attendance/<int:id>',employee.delete_attendance,name = 'delete_attendance'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
