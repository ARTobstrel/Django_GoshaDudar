from django.urls import path
from django.views.generic import ListView, DetailView

from .models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20]),

         name='news'),
    # path('', views.news, name='news'),

    path('<int:pk>/', DetailView.as_view(model=Articles), name='article'),
]
