from unittest import TestCase
from carrinho import Carrinho


class TestaCarrinho(TestCase):

    def setUp(self):
        self.carrinho = Carrinho()
        self.itens = {'Notebook': 1559.65, 'Celular': 2582.00, 'Teclado': 158.98, 'Caneta': 1.65, 'Mouse': 69.98,
                      'Grafites': 1.65}

        self.carrinho.add_item_carrinho(self.itens)
        self.menor = self.carrinho.menor_valor
        self.maior = self.carrinho.maior_valor

    def test_se_o_menor_valor_realmente_eh_o_menor(self):
        menor_esperado = 0
        for valor in self.itens.values():
            if menor_esperado == 0:
                menor_esperado = valor
            else:
                if valor < menor_esperado:
                    menor_esperado = valor

        self.assertEqual(menor_esperado, self.carrinho.menor_valor)

    def test_se_o_maior_valor_realmente_eh_o_maior(self):
        maior_esperado = 0
        for valor in self.itens.values():
            if maior_esperado == 0:
                maior_esperado = valor
            else:
                if valor > maior_esperado:
                    maior_esperado = valor

        self.assertEqual(maior_esperado, self.carrinho.maior_valor)

    def test_se_o_nome_do_produto_MENOR_eh_igual_do_menor_valor_esperado(self):
        nome_esperado = []
        for produto, valor in self.itens.items():
            if valor == self.menor:
                nome_esperado.append(produto.lower())

        self.assertEqual(nome_esperado, self.carrinho.menor_produto())

    def test_se_o_nome_do_produto_MAIOR_eh_igual_do_menor_valor_esperado(self):
        nome_esperado = []
        for produto, valor in self.itens.items():
            if valor == self.maior:
                nome_esperado.append(produto.lower())

        self.assertEqual(nome_esperado, self.carrinho.maior_produto())









