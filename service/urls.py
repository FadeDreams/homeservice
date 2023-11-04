
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.getAllServices, name='services'),
    path('services/new/', views.newService, name='new_service'),
    path('services/<str:pk>/', views.getService, name='service'),
    path('services/<str:pk>/update/', views.updateService, name='update_service'),
    path('services/<str:pk>/delete/', views.deleteService, name='delete_service'),
    path('stats/<str:topic>/', views.getTopicStats, name='get_topic_stats')
]
