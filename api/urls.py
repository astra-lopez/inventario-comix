from django.urls import path
from . import views

urlpatterns = [
  path('', views.ApiOverview, name='home'),
<<<<<<< HEAD
  path('create/', views.add_comic, name='add-comic'),
  path('all/', views.view_comics, name='view-comics'),
  path('update/<int:pk>/', views.update_comics, name='update-comics'),
  path('item/<int:pk>/delete/', views.delete_comics, name='delete-comics'),
=======
  path('comics/', views.view_comics, name='view-comics'),
  path('sales/', views.view_sales, name='view-sales'),
  path('comics/create/', views.add_comics, name='add-comics'),
  path('sales/create/', views.add_sales, name='add-sales'),
  path('comics/update/<int:pk>/', views.update_comics, name='update-comics'),
  path('sales/update/<int:pk>/', views.update_sales, name='update-sales'),
  path('comics/delete/<int:pk>/', views.delete_comics, name='delete-comics'),
  path('sales/delete/<int:pk>',views.delete_sales, name='delete-comics')
>>>>>>> d2b825cc98c9997984474e250d323f0c5dea2cae
]