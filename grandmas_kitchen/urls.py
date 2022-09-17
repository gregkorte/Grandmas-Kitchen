from django.urls import path, include
from grandmas_kitchen import views

urlpatterns = [
    path('', views.test, name='test')
]   