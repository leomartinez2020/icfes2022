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
