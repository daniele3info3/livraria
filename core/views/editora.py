from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core.serializers import EditoraSerializer

# from rest_framework.permissions import IsAuthenticated



class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
