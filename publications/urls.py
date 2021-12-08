# Publications URLs
from django.urls import path
from .views import PublicationView, ArticleView

urlpatterns = [
    path('', PublicationView.as_view(), name="publications"),
    path('<slug:slug>', ArticleView.as_view(), name='articles'),
    
]