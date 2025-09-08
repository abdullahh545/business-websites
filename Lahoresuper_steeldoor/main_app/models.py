from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"   # value saved in db, value shown to the user
        CUSTOMER = "customer", "Customer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=9999)
    price = models.IntegerField()
    category = models.CharField(max_length=255)  # fixed typo "catergory"

    is_active = models.BooleanField(default=True)
    product_image = models.ImageField(
        upload_to="service_images/",  # better to give a folder
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class ServiceBooking(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Confirmed", "Confirmed"),
            ("Completed", "Completed")
        ],
        default="Pending"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"
