class Carrinho():

    def __init__(self):
        self._lista = {}
        self._lista_zero = []
        self.lista_maior_produto = []
        self.lista_menor_produto = []


    @property
    def lista_itens(self):
        return self._lista

    def add_item_carrinho(self, itens):  # itens recebe um dicionário
        for produto, valor in itens.items():
            if valor != 0:
                self._lista[str(produto)] = float(valor)
            else:
                self._lista_zero.append(produto)

    def maior_menor(self):
        menor = maior = 0
        for produto, valor in self._lista.items():
            if (menor and maior) == 0:
                maior = valor
                menor = valor
            else:
                # Maior
                if valor >= maior:
                    maior = valor

                # Menor
                if valor <= menor:
                    menor = valor

        return menor, maior

    def menor_valor(self):
        return self.maior_menor()[0]

    def maior_valor(self):
        return self.maior_menor()[1]

    def produtos_valor_zero(self):
        return self.maior_menor()[2]

    @property
    def maior_produto(self):
        for produto, valor in self._lista.items():
            if valor == self.maior_valor():
                self.lista_maior_produto.append(produto)

        return f'Os produtos com MAIOR valor são: {self.lista_maior_produto}'

    @property
    def menor_produto(self):
        for produto, valor in self._lista.items():
            if valor == self.menor_valor():
                self.lista_menor_produto.append(produto)
        return f'Os produtos com MENOR valor são: {self.lista_menor_produto}'

    def __str__(self):
        if len(self._lista_zero) == 0:
            return f'Produtos: {self._lista}\nProdutos com valor igual a zero: NENHUM PRODUTO COM VALOR ZERO'
        else:
            return f'Produtos: {self._lista}\nProdutos com valor igual a zero: {self._lista_zero}'





