from django.urls import path
from myapp.views import home, about, contact, check_result

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('check_result/<str:task_id>', check_result, name='check_result'),
]
