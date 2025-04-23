from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('inventio_somos_todos/', views.inventio_somos_todos, name="inventio_somos_todos"),
    path('libros/', views.libros_lista, name="libros_lista"),
    path('recomendaciones/', views.recomendaciones, name="recomendaciones"),
    path('detalle_libro/<int:libro_id>/', views.detalle_libro, name="detalle_libro"),

]