from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adminlte import views as adminlte_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include("accounts.urls")), 
    path('accounts/', include("django.contrib.auth.urls")),   # working for login.html
    path('adminlte/', include('adminlte.urls')),
]

# Add the following lines to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)