from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bug/<int:id>/', views.bug_detail, name='bug_detail'),
    path('bug/create/', views.bug_create, name='bug_create'),
    path('bug/<int:id>/update/', views.bug_update, name='bug_update'),
    path('bug/<int:id>/delete/', views.bug_delete, name='bug_delete'),
]
