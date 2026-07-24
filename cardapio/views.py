from django.shortcuts import get_object_or_404, render

from .models import Cardapio, Produto





def cardapio_por_slug(request, slug):

    cardapio =  get_object_or_404(Cardapio, slug=slug)
    lanches = Produto.objects.filter(categoria__nome='Lanches', cardapio=cardapio)
    bebidas = Produto.objects.filter(categoria__nome='Bebidas', cardapio=cardapio)
    return render(request, "index.html", {'cardapio':cardapio, 'lanches': lanches, 'bebidas':bebidas})
