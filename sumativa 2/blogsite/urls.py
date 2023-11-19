from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),  # Añade esta línea para manejar la URL raíz
    path('admin/', admin.site.urls),
]
