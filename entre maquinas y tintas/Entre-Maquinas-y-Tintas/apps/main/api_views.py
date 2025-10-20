from rest_framework import viewsets
from .models import Machine, Ink
from .serializers import MachineSerializer, InkSerializer

class MachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint para consultar y editar máquinas.
    """
    queryset = Machine.objects.all().order_by('-created_at')
    serializer_class = MachineSerializer

class InkViewSet(viewsets.ModelViewSet):
    """
    API endpoint para consultar y editar tintas.
    """
    queryset = Ink.objects.all().order_by('-created_at')
    serializer_class = InkSerializer