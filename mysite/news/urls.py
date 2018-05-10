from django.urls import path
from django.views.generic import ListView

from .models import Articles
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20]),

         name='news'),
    # path('', views.news, name='news'),
]
