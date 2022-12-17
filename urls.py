from django.urls import path
from . import views

urlpatterns = [
    path('toys/', views.ToyList.as_view(), name='toy-list'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('organizations/', views.OrganizationList.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', views.OrganizationDetail.as_view(), name='organization-detail'),
]
