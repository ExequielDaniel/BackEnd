# blog/urls.py

from django.urls import path
from .views import index, post_detail, categoria_detail, hashtag_detail  # Asegúrate de tener el nombre correcto aquí

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('categoria/<int:categoria_id>/', categoria_detail, name='categoria_detail'),
    path('hashtag/<int:hashtag_id>/', hashtag_detail, name='hashtag_detail'),  # Asegúrate de tener el nombre correcto aquí
]
