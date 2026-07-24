from django.contrib import admin
from .models import Cardapio, Categoria, Produto


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ("lanchonete", "dono")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(dono=request.user)

  


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cardapio")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(cardapio__dono=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "cardapio" and not request.user.is_superuser:
            kwargs["queryset"] = Cardapio.objects.filter(
                dono=request.user
            )

        return super().formfield_for_foreignkey(
            db_field, request, **kwargs
        )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "cardapio", "preco")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(cardapio__dono=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "cardapio" and not request.user.is_superuser:
            kwargs["queryset"] = Cardapio.objects.filter(
                dono=request.user
            )

        if db_field.name == "categoria" and not request.user.is_superuser:
            kwargs["queryset"] = Categoria.objects.filter(
                cardapio__dono=request.user
            )

        return super().formfield_for_foreignkey(
            db_field, request, **kwargs
        )