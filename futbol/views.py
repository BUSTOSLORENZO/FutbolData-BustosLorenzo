from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Liga, Club, Jugador
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def index(request):

    return render(request,"index.html")


class LigaList(ListView):
    model = Liga
    template_name = "ligas.html"


class LigaCreate(CreateView):
    model = Liga
    fields = "__all__"
    template_name = "liga_form.html"
    success_url = "/ligas/"


class LigaUpdate(UpdateView):
    model = Liga
    fields = "__all__"
    template_name = "liga_form.html"
    success_url = "/ligas/"


class LigaDelete(DeleteView):
    model = Liga
    template_name = "liga_confirm_delete.html"
    success_url = "/ligas/"


class ClubList(ListView):
    model = Club
    template_name = "clubes.html"


class ClubCreate(CreateView):
    model = Club
    fields = "__all__"
    template_name = "club_form.html"
    success_url = "/clubes/"


class ClubUpdate(UpdateView):
    model = Club
    fields = "__all__"
    template_name = "club_form.html"
    success_url = "/clubes/"


class ClubDelete(DeleteView):
    model = Club
    template_name = "club_confirm_delete.html"
    success_url = "/clubes/"


class JugadorList(ListView):
    model = Jugador
    template_name = "jugadores.html"


class JugadorCreate(CreateView):
    model = Jugador
    fields = "__all__"
    template_name = "jugador_form.html"
    success_url = "/jugadores/"


class JugadorUpdate(UpdateView):
    model = Jugador
    fields = "__all__"
    template_name = "jugador_form.html"
    success_url = "/jugadores/"


class JugadorDelete(DeleteView):
    model = Jugador
    template_name = "jugador_confirm_delete.html"
    success_url = "/jugadores/"


def buscar_jugador(request):

    return render(request,"buscar.html")


def resultado_busqueda(request):

    nombre = request.GET.get("nombre")

    jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    clubes = Club.objects.filter(nombre__icontains=nombre)
    ligas = Liga.objects.filter(nombre__icontains=nombre)

    return render(request,"resultado_busqueda.html",
    {
        "jugadores": jugadores,
        "clubes": clubes,
        "ligas": ligas
    })

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/login")

    else:

        form = UserCreationForm()

    return render(request,"register.html",{"form":form})

def about(request):

    return render(request,"about.html")