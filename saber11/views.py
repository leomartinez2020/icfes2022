import csv
from django.http import HttpResponse
from saber11.models import Colegio
from saber11.serializers import ColegioSerializer
from rest_framework import generics
from rest_framework import permissions

class ColegioList(generics.ListCreateAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ColegioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def download(request):
    fields = ['nombre', 'codinst', 'municipio', 'codigomunicipio', 'departamento', 'calendario', 'naturaleza', 'evaluados', 'matematicas', 'sociales', 'ingles', 'ciencias', 'lectura', 'jornada', 'periodo', 'promponderado', 'puntajeglobal', 'slug']
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="colegios.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(fields)
    for col in Colegio.objects.all().values_list(*fields):
        writer.writerow(col)

    return response
