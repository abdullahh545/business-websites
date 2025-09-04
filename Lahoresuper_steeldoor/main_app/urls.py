from django.urls import path
from .views import (
    HomePageView,

    # Service views
    serviceListView, serviceDetailView, serviceCreateView,
    serviceUpdateView, serviceDeleteView,

    # ServiceBooking views
    serviceBookingListView, serviceBookingDetailView,
    serviceBookingCreateView, serviceBookingkUpdateView,
    serviceBookingkDeleteView,

    # Auth
    SignUpView,
)

urlpatterns = [
    # Home
    path("", HomePageView.as_view(), name="home"),

    # Service URLs
    path("services/", serviceListView.as_view(), name="service_list"),
    path("services/<int:pk>/", serviceDetailView.as_view(), name="service_detail"),
    path("services/create/", serviceCreateView.as_view(), name="service_create"),
    path("services/<int:pk>/update/", serviceUpdateView.as_view(), name="service_update"),
    path("services/<int:pk>/delete/", serviceDeleteView.as_view(), name="service_delete"),

    # ServiceBooking URLs
    path("bookings/", serviceBookingListView.as_view(), name="serviceBooking_list"),
    path("bookings/<int:serviceBooking_id>/", serviceBookingDetailView.as_view(), name="serviceBooking_detail"),
    path("bookings/create/", serviceBookingCreateView.as_view(), name="serviceBooking_create"),
    path("bookings/<int:serviceBooking_id>/update/", serviceBookingkUpdateView.as_view(), name="serviceBooking_update"),
    path("bookings/<int:serviceBooking_id>/delete/", serviceBookingkDeleteView.as_view(), name="serviceBooking_delete"),

    # Auth
    path("signup/", SignUpView.as_view(), name="signup"),
]
