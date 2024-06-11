from django.urls import path
from . import views

urlpatterns = [
  path('', views.ApiOverview, name='home'),
  path('create/', views.add_comic, name='add-comic'),
  path('all/', views.view_comics, name='view-comics'),
  path('update/<int:pk>/', views.update_comics, name='update-comics'),
  path('item/<int:pk>/delete/', views.delete_comics, name='delete-comics'),
]