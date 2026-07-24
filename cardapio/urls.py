from django.urls import path

from . import views


urlpatterns = [
    
    path("cardapio/<slug:slug>/", views.cardapio_por_slug, name="cardapio_por_slug"),
]
