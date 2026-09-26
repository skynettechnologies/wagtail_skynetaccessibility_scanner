from django.urls import path
from . import views

# app_name here is what provides the namespace (not the path() call)
app_name = 'wagtail_skynetaccessibility_scanner'

urlpatterns = [
    path('', views.scanner_dashboard, name='dashboard'),
]
