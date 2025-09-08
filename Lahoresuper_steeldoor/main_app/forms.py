from django import forms
from .models import Service, ServiceBooking, User
from django.contrib.auth.forms import UserCreationForm

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "price", "is_active", "category", "product_image"]  

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ["customer_name", "customer_email", "customer_phone", "service", "status"]


class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = ("username", "password1")  # Add other fields as needed