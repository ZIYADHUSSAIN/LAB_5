from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('add/', views.add_person, name='add_person'),
]
