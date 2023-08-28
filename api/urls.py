from django.urls import path
from . import views

urlpatterns = [
    path('get/<str:genre>/', views.getData),
    path('post/', views.addData),
]
