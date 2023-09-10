from django.urls import path
from . import views # '.' representa o diretório raiz

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('produto', views.detalhe_produto, name='produto'),
    path('teste', views.teste, name='teste'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   # Para carregar os arquivos de imagem cadastrados em DB
