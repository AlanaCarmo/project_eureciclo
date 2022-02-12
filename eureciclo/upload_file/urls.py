from django.urls import path
from . import views

app_name = 'upload_file'

urlpatterns = [
    path('upload', views.upload_file, name='upload'),
    path('report', views.report_file, name='reports')
]
