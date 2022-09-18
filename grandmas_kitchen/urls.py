from django.urls import path, include
from grandmas_kitchen import views

urlpatterns = [
    path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout')
]