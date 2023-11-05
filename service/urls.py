
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.getAllServices, name='services'),
    path('services/new/', views.newService, name='new_service'),
    path('services/<str:pk>/', views.getService, name='service'),
    path('services/<str:pk>/update/', views.updateService, name='update_service'),
    path('services/<str:pk>/delete/', views.deleteService, name='delete_service'),
    path('stats/<str:topic>/', views.getTopicStats, name='get_topic_stats'),
    path('services/<str:pk>/apply/', views.applyToService, name='apply_to_service'),
    path('me/services/applied/', views.getCurrentUserAppliedServices, name='current_user_applied_services'),
    path('me/services/', views.getCurrentUserServices, name='current_user_services'),
    path('services/<str:pk>/check/', views.isApplied, name='is_applied_to_service'),
    path('service/<str:pk>/candidates/', views.getUsersApplied, name='get_candidates_applied'),
]
