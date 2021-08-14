"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# usa-se o include para puxar urls de outros caminhos que não o padrão
from django.conf.urls import include
from django.urls import path
# Redirecionar a url raiz
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Puxará as urls referentes ao catalog e que estão internas
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/'))
]

# Para servir arquivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
