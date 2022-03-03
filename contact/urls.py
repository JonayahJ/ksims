# Contact URLs
from django.urls import path
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name="inquiry"),
    path('thankyou', views.thankyou, name="thankyou"),
]