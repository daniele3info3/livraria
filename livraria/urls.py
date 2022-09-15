from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register('autores', AutorViewSet)
router.register('categorias', CategoriaViewSet)
router.register('editoras', EditoraViewSet)
router.register('livros', LivroViewSet)


urlpatterns = [
    #Simple JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Admin
    path("admin/", admin.site.urls),
    #
    path('', include(router.urls)),
]
