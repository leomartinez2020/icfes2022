import json
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse

from visor.models import Colegio, Contacto

class CalendarioAListView(ListView):
    model = Colegio
    context_object_name = 'colegios'
    queryset = Colegio.objects.filter(periodo='2021').filter(promponderado__gt=68).filter(calendario='A').exclude(evaluados__lt=5).order_by('-promponderado')
    template_name = 'visor/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        #context['book_list'] = queryset
        context['year'] = '2021'
        context['calendario'] = 'A'
        return context


class CalendarioBListView(ListView):
    model = Colegio
    context_object_name = 'colegios'
    queryset = Colegio.objects.filter(periodo='2021').filter(promponderado__gt=68).filter(calendario='B').exclude(evaluados__lt=5).order_by('-promponderado')
    template_name = 'visor/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        #context['book_list'] = queryset
        context['year'] = '2021'
        context['calendario'] = 'B'
        return context

class ColegioListView(ListView):
    model = Colegio
    context_object_name = 'colegios'
    queryset = Colegio.objects.filter(periodo='2021').filter(promponderado__gt=68).exclude(evaluados__lt=5).order_by('-promponderado')
    template_name = 'visor/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        #context['book_list'] = queryset
        context['year'] = '2021'
        return context


class ColegioDetailView(DetailView):
    model = Colegio
    template_name = 'visor/detalle.html'

def colegio_detail_view(request, pk, slug):
    try:
        queryset = Colegio.objects.get(pk=pk)
        colegio = serializers.serialize("json", [queryset])
        #colegio = json.dumps(dict(queryset), cls=DjangoJSONEncoder)
    except Colegio.DoesNotExist:
        raise Http404('No hay tal colegio')

    return render(request, 'visor/detalle.html', context={'colegio_json': colegio, 'colegio': queryset})

def contacto(request):
    try:
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        contacto = Contacto(nombre=nombre, correo=correo, mensaje=mensaje)
        contacto.save()
        print(nombre)
    except:
        return render(request, 'main.html', {
            'error_message': "Los campos correo y mensaje son obligatorios.",
        })
    else:
        return HttpResponseRedirect(reverse('visor:mensaje_recibido'))

def mensaje_recibido(request):
    return render(request, 'mensaje_recibido.html')

def handle_page_not_found(request, exception):
    return render(request, 'page_not_found.html')
