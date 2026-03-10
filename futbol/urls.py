from django.urls import path
from . import views

urlpatterns = [

path("",views.index),

path("ligas/",views.LigaList.as_view()),
path("ligas/crear/",views.LigaCreate.as_view()),
path("ligas/editar/<int:pk>/",views.LigaUpdate.as_view()),
path("ligas/eliminar/<int:pk>/",views.LigaDelete.as_view()),

path("clubes/",views.ClubList.as_view()),
path("clubes/crear/",views.ClubCreate.as_view()),
path("clubes/editar/<int:pk>/",views.ClubUpdate.as_view()),
path("clubes/eliminar/<int:pk>/",views.ClubDelete.as_view()),

path("jugadores/",views.JugadorList.as_view()),
path("jugadores/crear/",views.JugadorCreate.as_view()),
path("jugadores/editar/<int:pk>/",views.JugadorUpdate.as_view()),
path("jugadores/eliminar/<int:pk>/",views.JugadorDelete.as_view()),

path("buscar/",views.buscar_jugador),
path("resultado/",views.resultado_busqueda),

path("register/",views.register),
path("about/",views.about),

]