from django.urls import path
from . import views

app_name = 'upload_file'

urlpatterns = [
    path('upload', views.upload_file, name='upload'),
    path('reports', views.report_file_all, name='reports'),
    path('report/<int:pk>', views.report_file, name='report')
]
