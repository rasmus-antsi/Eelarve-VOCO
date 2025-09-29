from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_transaction, name='create_transaction'),
    path('update/<uuid:id>/', views.update_transaction, name='update_transaction'),
    path('delete/<uuid:id>/', views.delete_transaction, name='delete_transaction'),
    path('get/<uuid:id>/', views.get_transaction, name='get_transaction'),
]