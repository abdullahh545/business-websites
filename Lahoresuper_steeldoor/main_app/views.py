from django.shortcuts import render
from .models import Service, ServiceBooking, User  # Use your custom User
from .forms import ServiceForm, ServiceBookingForm,CustomUserCreationForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = "service/service_list.html"
    context_object_name = "services"

class ServiceDetailView(DetailView):
    model = Service
    template_name = "service/service_detail.html"
    context_object_name = "service"

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "service/service_create.html"

    def get_success_url(self):
        return reverse("service_detail", kwargs={"pk": self.object.pk})

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "service/service_form.html"

    def get_success_url(self):
        return reverse("service_detail", kwargs={"pk": self.object.pk})

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = "service/service_confirm_delete.html"
    success_url = reverse_lazy("service_list")



class ServiceBookingListView(ListView):
    model = ServiceBooking
    template_name = "serviceBooking/serviceBooking_list.html"
    context_object_name = "serviceBookings"

class ServiceBookingDetailView(DetailView):
    model = ServiceBooking
    template_name = "serviceBooking/serviceBooking_detail.html"
    context_object_name = "serviceBooking"
    pk_url_kwarg = "serviceBooking_id"  

class ServiceBookingCreateView(LoginRequiredMixin, CreateView):
    model = ServiceBooking
    form_class = ServiceBookingForm
    template_name = "serviceBooking/serviceBooking_create.html"

    def get_success_url(self):
        return reverse("serviceBooking_detail", kwargs={"serviceBooking_id": self.object.pk})

class ServiceBookingUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceBooking
    form_class = ServiceBookingForm
    template_name = "serviceBooking/serviceBooking_create.html"
    pk_url_kwarg = "serviceBooking_id"

    def get_success_url(self):
        return reverse("serviceBooking_detail", kwargs={"serviceBooking_id": self.object.pk})

class ServiceBookingDeleteView(DeleteView):
    model = ServiceBooking
    template_name = "serviceBooking/serviceBooking_confirm_delete.html"
    success_url = reverse_lazy("serviceBooking_list")



class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class SignUpView(CreateView):
    model=User
    form_class = CustomUserCreationForm
    template_name='registration/sign-up.html'
    success_url = reverse_lazy('home')

