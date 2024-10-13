from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('cars/',views.car_list_view, name='car-list'),
    path('car/<str:car_id>/',views.car_detail_view, name='car-detail'),
    path('car/add/',views.add_car_view, name='add-car'),
    path('car/delete/<str:car_id>/',views.delete_car_view, name='delete-car'),

]

