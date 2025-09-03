from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

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

class service(models.Model):
    name =  models.CharField(max_length=120)
    description =  models.CharField(max_length=9999)
    price =  models.IntegerField()
    catergory =  models.CharField(max_length=99999)

    is_Active = models.BooleanField(default=True)
    product_image = models.ImageField(
    upload_to=None, 
    height_field=None, 
    width_field=None, 
    max_length=100, 
)
    
class serviceBooking(models.Model):
        customer_name = models.CharField(max_length=200)
        customer_email = models.EmailField()
        customer_phone = models.CharField(max_length=15)
        service = models.ForeignKey(service, on_delete=models.CASCADE)
        date_requested = models.DateTimeField(auto_now_add=True)
        status = models.CharField(
            max_length=20,
            choices=[("Pending", "Pending"), ("Confirmed", "Confirmed"), ("Completed", "Completed")],
            default="Pending"
        )

        def _str_(self):
         return f"{self.customer_name} - {self.service.name}"











