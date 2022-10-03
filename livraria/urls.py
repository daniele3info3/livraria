from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from media.router import router as media_router

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
    path('api/media/', include(media_router .urls)),
]

# urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)