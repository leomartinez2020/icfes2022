from rest_framework import serializers
from saber11.models import Colegio

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = ['pk', 'nombre', 'codinst', 'municipio', 'departamento', 'calendario', 'naturaleza',
                  'evaluados', 'matematicas', 'sociales', 'ingles', 'ciencias', 'lectura', 'promponderado',
                  'puntajeglobal', 'periodo']
