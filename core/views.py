from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from . models import Produto


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_adicionar.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

    def form_valid(self,*args):
        messages.success(self.request, 'Produto cadastrado com sucesso')
        return super(CreateProdutoView, self).form_valid(*args)
    
    def form_invalid(self, *args):
        messages.error(self.request, 'Erro ao cadastrar o produto')
        return super(CreateProdutoView, self).form_invalid(*args)


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_editar.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

    def form_valid(self, *args):
        messages.success(self.request, 'Produto editado com sucesso')
        return super(UpdateProdutoView, self).form_valid(*args)
    
    def form_invalid(self, *args):
        messages.error(self.request, 'Erro ao editar o produto')
        return super(UpdateProdutoView, self).form_invalid(*args)
    

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_excluir.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args):
        messages.success(self.request, 'Produto excluído com sucesso')
        return super(DeleteProdutoView, self).form_valid(*args)
    
    def form_invalid(self, *args):
        messages.error(self.request, 'Erro ao excluir o Produto')
        return super(DeleteProdutoView, self).form_invalid(*args)