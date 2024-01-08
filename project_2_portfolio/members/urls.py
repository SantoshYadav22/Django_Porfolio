from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('example/<str:optional_param>/', views.filter_user, name='example_optional'),
    path('members/index/', views.index, name='index'),
    path('your-form/', views.create_user, name='your_form_view'),
    # path('members/view/<int:pk>/', views.view_member, name='view_member'),
    path('members/delete/<int:pk>/', views.delete_member, name='delete_member'),
]