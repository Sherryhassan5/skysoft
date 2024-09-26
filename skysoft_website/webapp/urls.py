from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('career/', career, name='career'),
    path('job/<int:id>/', job, name='job'),
    path('job-application/<int:id>/', job_application, name='job-application'),
    path('contact', contactus, name='contactus'),
    path('contact/', contact_project, name='contact_project'),
]
