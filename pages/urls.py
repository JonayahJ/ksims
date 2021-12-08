# Pages URL Configuration
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('perceived-discrimination', views.perceived_discrimination, name="perceived_discrimination"),
    path('health-retirement', views.health_retirement, name="health_retirement"),
    path('jackson-heart', views.jackson_heart, name="jackson_heart"),
]