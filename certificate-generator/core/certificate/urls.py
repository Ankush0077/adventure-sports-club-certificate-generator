from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificate/<int:pk>/', views.certificate, name='certificate'),
    path('certificate_image/<int:pk>', views.certificateImage, name='certificate-image')
]