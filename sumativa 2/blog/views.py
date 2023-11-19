from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Hashtag


def index(request):
    ultima_publicacion = Post.objects.last()
    publicaciones = Post.objects.all()
    categorias = Category.objects.all()
    hashtags = Hashtag.objects.all()
    return render(request, 'index.html', {
        'ultima_publicacion': ultima_publicacion,
        'publicaciones': publicaciones,
        'categorias': categorias,
        'hashtags': hashtags
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'post_detail.html', {'post': post})


def categoria_detail(request, categoria_id):
    categoria = get_object_or_404(Category, pk = categoria_id)
    return render(request, 'categoria_detail.html', {'categoria': categoria})


def hashtag_detail(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk = hashtag_id)
    return render(request, 'hashtag_detail.html', {'hashtag': hashtag})