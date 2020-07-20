from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('<int:show_id>', views.show),
    path('edit/<int:show_id>/', views.edit),
    path('create', views.create),
    path('<int:show_id>/update/', views.update),
    path('delete/<int:show_id>/', views.delete),
]