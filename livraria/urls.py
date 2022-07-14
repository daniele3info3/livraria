from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('editoras', EditoraViewSet)
router.register('livros', LivroViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
