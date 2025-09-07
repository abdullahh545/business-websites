from django.urls import path
from .views import (
    HomePageView,

    ServiceListView, ServiceDetailView, ServiceCreateView,
    ServiceUpdateView, ServiceDeleteView,

    ServiceBookingListView, ServiceBookingDetailView,
    ServiceBookingCreateView, ServiceBookingUpdateView,
    ServiceBookingDeleteView,

    SignUpView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path("services/", ServiceListView.as_view(), name="service_list"),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("services/create/", ServiceCreateView.as_view(), name="service_create"),
    path("services/<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"),
    path("services/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"),

    path("bookings/", ServiceBookingListView.as_view(), name="serviceBooking_list"),
    path("bookings/<int:serviceBooking_id>/", ServiceBookingDetailView.as_view(), name="serviceBooking_detail"),
    path("bookings/create/", ServiceBookingCreateView.as_view(), name="serviceBooking_create"),
    path("bookings/<int:serviceBooking_id>/update/", ServiceBookingUpdateView.as_view(), name="serviceBooking_update"),
    path("bookings/<int:serviceBooking_id>/delete/", ServiceBookingDeleteView.as_view(), name="serviceBooking_delete"),

    path("signup/", SignUpView.as_view(), name="signup"),
    # path("login/", LoginView.as_view(), name="login"),

]
