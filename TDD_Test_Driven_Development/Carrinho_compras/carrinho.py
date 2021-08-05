class Carrinho():

    def __init__(self):
        self._lista = {}

    def add_item_carrinho(self, nome, valor ):
        if valor != 0:
            self._lista[str(nome)] = float(valor)
        else:
            raise ValueError('Valor não pode ser zero')

    def maior_menor(self):
        menor = maior = 0
        for produto, valor in self._lista.items():
            if (menor and maior) == 0:
                maior = valor
                menor = valor
            else:
                # Menor
                if valor > maior:
                    maior = valor
                # Meior
                if valor <= menor:
                    menor = valor
                    menor_produto = produto

        return menor, maior

    def menor_valor(self):
        return self.maior_menor()[0]

    def maior_valor(self):
        return self.maior_menor()[1]

    def maior_produto(self):
        global maior_produto
        for produto, valor in self._lista.items():
            if valor == self.maior_valor():
                maior_produto = produto
        return maior_produto

    def menor_produto(self):
        global menor_produto
        for produto, valor in self._lista.items():
            if valor == self.menor_valor():
                menor_produto = produto
        return menor_produto

    def __str__(self):
        return f'{self._lista}'




