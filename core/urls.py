from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produto_adicionar/', CreateProdutoView.as_view(), name='produto_adicionar'),
    path('produto_editar/<int:pk>', UpdateProdutoView.as_view(), name='produto_editar'),
    path('produto_excluir/<int:pk>', DeleteProdutoView.as_view(), name='produto_excluir'),
]
