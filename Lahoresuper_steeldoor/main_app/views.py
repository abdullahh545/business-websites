from django.shortcuts import render
from.models import serviceBooking, service
from .forms import ServiceForm, ServiceBookingForm

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class serviceListView(LoginRequiredMixin,ListView):
    model = service
    template_name = "service/service_list.html"
    context_object_name = "service"


    def get_queryset(self):
        return super().get_queryset()


class serviceDetailView(DetailView):
    model = service
    template_name = "service/service_detail.html"
    context_object_name = "service"



class serviceCreateView(CreateView):
    model = service
    form_class = service
    template_name = "service/service_form.html"


    def get_success_url(self):
        return reverse("service_detail", kwargs={"pk": self.object.pk})


class serviceUpdateView(UpdateView):
    model = service
    form_class = ServiceForm
    template_name = "service/service_form.html"

    def get_success_url(self):
        return reverse("service_detail", kwargs={"pk": self.object.pk})


class serviceDeleteView(DeleteView):
    model = service
    template_name = "service/service_confirm_delete.html"
    success_url = reverse_lazy("service_list")





class serviceBookingCreateView(LoginRequiredMixin,CreateView):
    model = serviceBooking
    template_name = 'serviceBooking/serviceBookingform.html'
    form_class = ServiceBookingForm

    def get_success_url(self):
        return reverse('serviceBooking_detail',kwargs={'serviceBooking_id':self.object.pk})

class serviceBookingListView(ListView):
    model = serviceBooking
    template_name = 'serviceBooking/serviceBooking_list.html'
    context_object_name = 'serviceBooking'


class serviceBookingkUpdateView(LoginRequiredMixin,UpdateView):
    model = serviceBooking
    template_name = 'serviceBooking/serviceBookingform.html'
    form_class = ServiceBookingForm
    success_url = "/booserviceBooking/"
    pk_url_kwarg = 'serviceBooking_id' #change the dynamic url in the urls.py


class serviceBookingDetailView(DetailView):
    model = serviceBooking
    template_name = 'serviceBooking/serviceBooking_detail.html'
    context_object_name = 'serviceBooking'
    pk_url_kwarg = 'serviceBooking_id' #change the dynamic url in the urls.py


# Gets the favorites for the user for this book if he did favorite it
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['did_favorite'] = serviceBooking.objects.filter(user = user, serviceBooking = self.object).exists()
        return ctx


class serviceBookingkDeleteView(DeleteView):
    model = serviceBooking
    success_url = "/serviceBooking/"





from django.views.generic import TemplateView
from .models import Service

class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()   # pass all services to template
        return context


    








from django.contrib.auth.models import User # this is the user model we use to log in
from django.contrib.auth.forms import UserCreationForm
class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/sign-up.html'
    






