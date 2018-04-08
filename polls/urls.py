from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_check, name='Current Challenge'),
    path('info/', views.info, name='About'),
    path('admin-panel/', views.admin_panel, name='Admin Panel'),
    path('update/', views.update_users, name='update'),
    path('students/', views.display_students, name='Studen List`'),
    path('reset/', views.reset_users_progress, name='Reset Student Progress')
]
