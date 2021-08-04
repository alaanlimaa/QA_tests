import sys


class Usuario:

    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor > self._carteira:
            raise ValueError('Não pode propor o lance maior que o da carteira')
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self._carteira -= valor


    @property
    def nome(self):
        return self._nome

    @property
    def carteira(self):
        return self._carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self._lances = []
        self.menor_lance = sys.float_info.max
        self.maior_lance = sys.float_info.min

    def propoe(self, lance: Lance):

        if not self._lances or self._lances[-1].usuario != lance.usuario and lance.valor > self._lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self._lances.append(lance)

        else: #exceção
            raise ValueError('ERRO ao propor lance')


    @property
    def lances(self):
        return self._lances[:] # [:] devolve uma cópia da lista, chamado também de cópia rasa (pesquisar o que é)







