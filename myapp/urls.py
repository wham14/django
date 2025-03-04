from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),

    path('mit/', views.mit, name='mit'),

    path('contactus/', views.contact, name='contact'),

    path( 'gallery/', views.gallery, name='gallery'),

    path('services', views.services, name='services'),


]
