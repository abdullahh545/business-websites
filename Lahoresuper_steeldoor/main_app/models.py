from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class product(models.Model):
    name =  models.CharField(max_length=120)
    description =  models.CharField(max_length=9999)
    price =  models.IntegerField()
    catergory =  models.CharField(max_length=99999)
    
    product_image = models.ImageField(
    upload_to=None, 
    height_field=None, 
    width_field=None, 
    max_length=100, 
)



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        CUSTOMER = "customer", "Customer"
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
         default=Role.CUSTOMER,
        null=True
    )