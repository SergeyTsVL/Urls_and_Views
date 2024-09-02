from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('class/', views.index, name='index'),
    path('func/', views.index1, name='index1'),
]