class Carrinho():

    def __init__(self):
        self._lista = {}
        self._lista_zero = []
        self.lista_maior_produto = []
        self.lista_menor_produto = []

    @property
    def lista_itens(self):  # retorna apenas os itens com respectivos valores diferente de ZERO
        return self._lista

    @property
    def lista_zero(self):  # retorna apenas os itens com respectivos valores igual a ZERO
        return self._lista_zero

    def view_carrinho(self):
        print(self.__str__())

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

    @property
    def menor_valor(self):
        return self.maior_menor()[0]

    @property
    def maior_valor(self):
        return self.maior_menor()[1]

    def maior_produto(self):  # saída será uma lista com os maiores produtos
        for produto, valor in self._lista.items():
            if valor == self.maior_valor:
                self.lista_maior_produto.append(produto.lower())
        return self.lista_maior_produto

    def view_lista_maior_produto(self):  # Apenas apresentação da lista de produtos com maiores valores
        print(f'Os maiores produtos são: {self.maior_produto()}')

    def menor_produto(self):  # saída será uma lista com os menores produtos
        for produto, valor in self._lista.items():
            if valor == self.menor_valor:
                self.lista_menor_produto.append(produto.lower())
        return self.lista_menor_produto

    def view_lista_menor_produto(self):  # Apenas apresentação da lista de produtos com menores valores
        print(f'Os menores produtos são: {self.menor_produto()}')

    def __str__(self):
        if len(self._lista_zero) == 0:
            return f'Produtos: {self._lista}\nProdutos com valor igual a zero: NENHUM PRODUTO COM VALOR ZERO'
        else:
            return f'Produtos: {self._lista}\nProdutos com valor igual a zero: {self._lista_zero}'
