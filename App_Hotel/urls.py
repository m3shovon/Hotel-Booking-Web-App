from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('book/<int:room_id>/', views.book_hotel, name='book_hotel'),
    path('payment/', views.payment, name='payment'),
]
