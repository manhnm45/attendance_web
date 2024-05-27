from django.db import models

# Create your models here.
class employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null = False,unique=True)
    position = models.CharField(max_length=30, null = False)
    # avata = models.ImageField(upload_to='Image' , null= False, default= None)
    # file_image = models.FileField(upload_to= 'folder', null= False, default= None)
    avata = models.CharField(max_length=30, null = False,default= None)
    file_image = models.CharField(max_length=30, null = False, default= None)
    def __str__(self):
        return f"{self.employees_id}, {self.name}, {self.position}, {self.avata}, {self.file_image} "
    

class attendance(models.Model):
    employee = models.ForeignKey(employees, on_delete= models.CASCADE,to_field='employees_id')
    date = models.CharField()
    time_in = models.CharField()
    time_out = models.CharField( null=True)
    location_check = models.CharField(max_length=30)
    
    @property
    def name(self):
        return self.employee.name
    @property
    def id_staff(self):
        return self.employee.employees_id
    
    def __str__(self):
        
        return f"{self.employee.name}, {self.date}, {self.time_in}, {self.time_out}, {self.location_check} "


