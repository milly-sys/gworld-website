from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('company-profile/', views.company_profile, name='company_profile'),
    path('why-us/', views.why_us, name='why_us'),
]