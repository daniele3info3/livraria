from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroDetailSerializer, LivroSerializer

# from rest_framework.permissions import IsAuthenticated



class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    #  serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrive"]:
            return LivroDetailSerializer
        return LivroSerializer