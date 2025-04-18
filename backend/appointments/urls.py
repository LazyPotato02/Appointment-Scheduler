from django.urls import path
from .views import AppointmentViewSet, GetSignalerAppointment, GetReservedSlots, GetAppointmentByDateTime

urlpatterns = [
    path('', AppointmentViewSet.as_view(), name='appointments'),
    path('<int:id>/', GetSignalerAppointment.as_view(), name='appointment-detail'),
    path('reserved/<str:date>/', GetReservedSlots.as_view(), name='reserved-appointments'),
path('<str:date>/<str:time>/', GetAppointmentByDateTime.as_view(), name='appointment_by_datetime'),
]
