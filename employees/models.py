from django.db import models

# Create your models here.
class employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null = False)
    position = models.CharField(max_length=30, null = False)
    # avata = models.ImageField(upload_to='Image' , null= False, default= None)
    # file_image = models.FileField(upload_to= 'folder', null= False, default= None)
    avata = models.CharField(max_length=30, null = False,default= None)
    file_image = models.CharField(max_length=30, null = False, default= None)
    def __str__(self):
        return f"{self.employees_id}, {self.name}, {self.position}, {self.avata}, {self.file_image} "
