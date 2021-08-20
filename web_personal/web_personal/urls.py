from django.contrib import admin
from django.urls import path
from core import views
from portfolio.views import portfolio
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about , name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

# Si estamos en modo de desarrollo osea estamos en debug, agregamos una ruta nueva al urlpatterns
# La misma está compuesta por la url de media, osea MEDIA_URL, y la raiz MEDIA_ROOT
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
