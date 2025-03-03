from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),

    path('mit/', views.mit, name='mit'),

    path('contactus/', views.contact, name='contact'),


]
