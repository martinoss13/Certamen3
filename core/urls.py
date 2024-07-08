from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="index"),
    path('nuevo_registro/', views.registro, name= "nuevo_registro"),
    path('editar_registro/<int:registro_id>/', views.registro, name= "editar_registro"),

]