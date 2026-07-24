from django.test import TestCase

from .models import Cardapio, Categoria, Produto


class CardapioTests(TestCase):
    def test_home_exibe_os_produtos_do_cardapio(self):
        cardapio = Cardapio.objects.create(
            lanchonete="RedBurger",
            endereco="Rua Principal, 1",
            disponivel="Todos os dias",
            slug="redburger",
        )
        categoria = Categoria.objects.create(nome="Lanches")
        Produto.objects.create(
            capa="foto_produto/teste.png",
            titulo="X-Burger",
            desc="Hambúrguer artesanal",
            preco="25.00",
            categoria=categoria,
            cardapio=cardapio,
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RedBurger")
        self.assertContains(response, "X-Burger")
